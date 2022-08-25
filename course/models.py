## @brief Models for the course app.

from curses import def_prog_mode
from django.db import models
from django.contrib.auth.models import User
from django.forms import EmailField
from instructor.models import Course
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import format_html


## @brief This class represents the students enrolled in the website.
class Student(models.Model):
    ## The user associated with the student
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField(max_length=256)
    ## The name of the student
    name = models.CharField(max_length=100)
    
    ## The roll number the student
    roll_no = models.CharField(max_length=100)
    ## The courses undertaken by the student
    course_list = models.ManyToManyField(Course)
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
    def get_coursesl(self):
        if self.course_list:
            return ",".join([str(p) for p in self.course_list.all()])
        else:
            return format_html('User has no Profile image to display'
            )

    def admin_photo(self):
        if self.profile_pic:
            return mark_safe('<img src="{}" width="150" height="150"/>'.format(self.profile_pic.url))
        else:
            return format_html('User has no Profile image to display'
            )
    admin_photo.short_description = 'Profile Image'
    admin_photo.allow_tags = True

    
    
    

    ## @brief This function returns the string representation of the student class.
    #
    # Used by Django admin website to represent the Student objects.
    # @param self The object pointer.
    def __str__(self):
        return self.name


## @brief This class represents the messages displayed in the forum.
class Message(models.Model):
    content = models.CharField(max_length=500)
    course = models.ForeignKey(Course,default=1,on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User,default=1, on_delete=models.SET_NULL, null=True)
    
    time = models.CharField(max_length=100)


## @brief This class represents the notifications receieved by the students.
class Notification(models.Model):
    ## The content of notification
    content = models.CharField(max_length=500)

    ## The course associated with the notification
    course = models.ForeignKey(Course, default=1, on_delete=models.SET_NULL, null=True)

    ## The time when the notification was posted/generated
    time = models.CharField(max_length=100)


## @brief This class represents the resources(lectures/study materials) for a course.
class Resources(models.Model):
    ## The resource file 
    file_resource = models.FileField(default='')
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    ## The title for the resource
    title = models.CharField(max_length=100)

    ## The course associated with the resource
    course = models.ForeignKey(Course, default=1, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Resources"


class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile' )

