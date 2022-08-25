## @brief Models for the instructor app.
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator


class Instructor(models.Model):
    ## The user associated with the instructor
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    information = models.CharField(max_length=1000,default=1)
    email = models.EmailField(max_length=256,default='student@bic.edu.np')
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
   
    def __str__(self):
        return self.name
    
    def admin_photo(self):
        if self.profile_pic:
            return mark_safe('<img src="{}" width="150"  height ="150"/>'.format(self.profile_pic.url))
        else:
            return format_html('No Image to Display'
            )
    admin_photo.short_description = 'Profile Image'
    admin_photo.allow_tags = True

## @brief This class represents the courses.
class Course(models.Model):
    ## The name of the course
    name = models.CharField(max_length=100)

    ## The course code
    code = models.CharField(max_length=100)

    ## The instructor of the course
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    ## The course logo
    course_logo = models.FileField(default=1)

    ## @brief This function returns the string representation of the course class.
    #
    # Used by Django admin website to represent the course objects.
    def __str__(self):
        return self.name

    def admin_photo(self):
        if self.course_logo:
            return mark_safe('<img src="{}" width="150" />'.format(self.course_logo.url))
        else:
            return format_html('No Image to Display'
            )
    admin_photo.short_description = 'Course Logo'
    admin_photo.allow_tags = True


## @brief This class represents the assignments in a course.
class Assignment(models.Model):
    ## The description of the assignment
    description = models.CharField(max_length=1000, default='')

    ## The file containing the problems for the assignment
    file = models.FileField(default='')

    ## The course associated with the assignment
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    ## The date,time of posting the assignment
    post_time = models.CharField(max_length=100)

    ## The deadline to complete the assignment for the students
    deadline = models.CharField(max_length=100)

    def __str__(self):
        return self.description

## @brief This class represents the submissions for an assignment.
class Submission(models.Model):
    ## The file submitted by student
    file_submitted = models.FileField(default='')

    ## The date,time of uploading the submission
    time_submitted = models.CharField(max_length=100)

    ## The user associated with the submission(who uploaded the submission)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    ## The assignment associated with the submission
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return str(self.file_submitted)


class Grades(models.Model):
    Submission=models.ForeignKey(Submission,on_delete=models.CASCADE,default=1)
    grade= models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )

class Feedback(models.Model):
    description = models.CharField(max_length=1000, default='')
    submission=models.ForeignKey(Submission,on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    grade= models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )

    def __str__(self):
        return self.description



