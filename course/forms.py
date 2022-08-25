## @brief Forms for the course app.

from django import forms
from django.contrib.auth.models import User

from .models import Message, Student
from instructor.models import Submission


## @brief This class represents the form to send a message in the forum.
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']


## @brief This class represents the form to add a submission for an assignment.
class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['file_submitted']

class SubmissionUpdate(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['file_submitted']
        

class StudentprofileUpdate(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name','roll_no','profile_pic']
