
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index,name="index"),
    path('index.html', views.index,name="index"),
    path('contact.html', views.contact_us,name="contact"),
    path('about.html', views.about,name="about"),
    path('view.html', views.view,name="view"),
    path('SignupPage.html', views.SignupPage,name="SignupPage"),
    path('', views.LoginPage,name="LoginPage"),
    path('logout', views.LogoutPage,name="logout"),
    path('LoginPage.html', views.LoginPage,name="LoginPage"),
     path('detect/', views.detect, name='detect'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
