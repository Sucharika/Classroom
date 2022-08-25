## @brief Forms for the course app.
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.contrib.auth.models import User

from .models import Assignment, Grades,Instructor,Feedback
from course.models import Notification, Resources

## @brief This class represents the form to add a notification.
class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']


## @brief This class represents the form to add an assignment.
class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['description', 'file', 'deadline']
        widgets = {
            'deadline': forms.NumberInput(attrs={'type': 'date'})
        } 
class AssignmentUpdate(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['description', 'file', 'deadline']
        widgets = {
            'deadline': forms.NumberInput(attrs={'type': 'date'})
        } 


## @brief This class represents the form to add a resource.
class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ['title', 'file_resource']

class ResourceUpdate(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ['title', 'file_resource']

class InstructorProfileUpdate(forms.ModelForm):
    class Meta():
        model = Instructor
        fields = ['name','email','profile_pic']

class GradingForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = "__all__"

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['description','grade']

class FeedbackUpdate(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['description','grade']


