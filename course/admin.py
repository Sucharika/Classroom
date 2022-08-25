## @brief The models registered for the admin site

from django.contrib import admin
from .models import Student, Message, Notification, Resources
from  django.contrib.auth.models  import  Group  

admin.site.unregister(Group) 

class StudentsAdmin(admin.ModelAdmin):
    fields = ('user','name','admin_photo','profile_pic','roll_no','email','course_list')
    list_display =[
        'user',
        'admin_photo',
        'name',
        'roll_no',
        'email',
        'get_coursesl'
    ]
    readonly_fields = ['admin_photo']

admin.site.register(Student,StudentsAdmin)

class MessagesAdmin(admin.ModelAdmin):
    fields = ('content','course','sender','time')
    list_display =[
        'content','course','sender','time'
    ]
    readonly_fields = ['time' ,'sender']

admin.site.register(Message,MessagesAdmin)

class NotificationssAdmin(admin.ModelAdmin):
    fields = ('content','course','time')
    list_display =[
        'content','course','time'
    ]
    readonly_fields = ['time']

admin.site.register(Notification,NotificationssAdmin)

class ResourcessAdmin(admin.ModelAdmin):
    fields = ('title','file_resource','course','user')
    list_display =[
        'title','file_resource','course','user'
    ]
    readonly_fields = ['course']

admin.site.register(Resources,ResourcessAdmin)
