from django.contrib import admin
from myapp.models import Contact
from myapp.models import UserInfo

# Register your models here.
admin.site.site_header = "AJCS_Detection | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject','message','added_on','is_approved']

class useradmin(admin.ModelAdmin) :
    list_display=['Uname','Email']

admin.site.register(Contact, ContactAdmin)
admin.site.register(UserInfo,useradmin )

# class RecipeAdmin(admin.ModelAdmin):
#     list_display=['id','recipe_name','recipe_ingredients','recipe_description','recipe_image']

#admin.site.register(Recipe)
