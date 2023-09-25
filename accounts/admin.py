from django.contrib import admin
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdmin(UserAdmin):
    filter_horizontal = ()
    list_display =['email','first_name', 'last_name','username','role', 'is_active','is_admin','date_joined','last_login']
    list_display_links=['email','first_name', 'last_name','username']
    readonly_fields = ['created_date','date_joined','modified_date','last_login']
    ordering=('-date_joined',)
    list_filter=()
    search_fields = ['email','first_name','last_name','username']
    
    fieldsets=(
        ('Password',{'fields':['password']}),
        ('Personal Informations',{'fields':['first_name', 'last_name', 'username', 'email','phone_number']}),
        ('Role',{'fields':['role']}),
        ('Permisions',{'fields':['is_active', 'is_staff','is_admin','is_superuser']}),
        ('Dates',{'fields':['created_date','date_joined','modified_date','last_login']})
    )

class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ()
    list_display=['user','country','county','city','postcode','latitude','longitude']
    list_display_links=['user','country','county','city','postcode']   
    readonly_fields=['created_at','modified_at']
    ordering=('-created_at',)
    list_filter=()
    search_fields=('user.email',)

    fieldsets=(
        ('User',{'fields':['user','profile_picture','cover_photo']}),
        ('Address',{'fields':['address_line_1','address_line_2','country','county','city','postcode']}),
        ('Geographical Location',{'fields':['latitude','longitude']}),
        ('Dates',{'fields':['created_at','modified_at']}),
    )


admin.site.register(User,UserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)