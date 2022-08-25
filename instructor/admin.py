from django.contrib import admin
from .models import Feedback, Instructor, Course, Assignment, Submission,Feedback

class InstructorsAdmin(admin.ModelAdmin):
    fields = ('user','name','admin_photo','profile_pic','information','email')
    list_display =[
        'user',
        'admin_photo',
        'name',
        'information',
        'email',
    ]
    readonly_fields = ['admin_photo']

admin.site.register(Instructor,InstructorsAdmin)

class AssignmentssAdmin(admin.ModelAdmin):
    fields = ('description','file','deadline','post_time','course')
    list_display =[
        'description',
        'deadline','post_time','course'
    ]
    readonly_fields = ['course']

admin.site.register(Assignment,AssignmentssAdmin)

class CoursesAdmin(admin.ModelAdmin):
    fields = ('name','admin_photo','course_logo','code','instructor')
    list_display =[
        'name','admin_photo','code','instructor'
    ]
    readonly_fields = ['admin_photo']

admin.site.register(Course,CoursesAdmin)

class FeedbacksAdmin(admin.ModelAdmin):
    fields = ('description','grade','user','submission')
    list_display =[
        'description','grade','user','submission'
    ]
    readonly_fields = ['user','submission'
    ]

admin.site.register(Feedback,FeedbacksAdmin)


class SubmissionsAdmin(admin.ModelAdmin):
    fields = ('file_submitted','time_submitted','user','assignment')
    list_display =[
        'time_submitted','file_submitted','user','assignment'
    ]
    readonly_fields = ['user','file_submitted']
admin.site.register(Submission,SubmissionsAdmin)