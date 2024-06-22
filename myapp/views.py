import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress INFO and WARNING messages

from django.shortcuts import render, redirect
from myapp.models import Contact
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import tensorflow as tf
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from keras.models import load_model
from PIL import Image
from django.conf import settings
from keras.preprocessing.image import load_img, img_to_array


# Create your views here.
@login_required(login_url='LoginPage')
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def view(request):
    return render(request, 'view.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your Time"
    return render(request, 'contact.html',context)


def SignupPage(request):
    if request.method=="POST":
        name = request.POST.get("uname")
        email = request.POST.get("uemail")
        password = request.POST.get("upass")
        passwordc = request.POST.get("upassc")

        if password!=passwordc:
            return HttpResponse("Your password and confirm pass not same")
        else:
            my_user=User.objects.create_user(name,email,password)
            my_user.save()
        return redirect('LoginPage.html')
    return render(request, 'SignupPage.html')

def LoginPage(request):
    if request.method=="POST":
        username = request.POST.get("username")
        passu = request.POST.get("passu")
        user=authenticate(request,username=username,password=passu)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'LoginPage.html')

def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')


# Load the model once at the start
model_path = os.path.join('media', 'my_model.keras')

try:
    # Load the model once at the start
    model = load_model(model_path, compile=False)
except ValueError as e:
    model = None
    print(f"Error loading model: {e}")
#model.load_weights('model.weights.h5.keras')

@csrf_exempt
def detect(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        img = Image.open(file)#.convert('L')
        img = img.convert('RGB')  # Convert to RGB mode (3 channels)
        img = img.resize((150,150))

        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)
        result = np.argmax(predictions, axis=1)[0]

        return JsonResponse({'result': int(result)})
    return JsonResponse({'error': 'Invalid request'}, status=400)