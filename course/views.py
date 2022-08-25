## @brief Views for the course app.

from django.contrib.auth.decorators import login_required

import course
from .models import Student, Message, Notification, Resources
from instructor.models import Assignment, Course, Instructor,Submission ,Feedback
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import MessageForm, StudentprofileUpdate, SubmissionForm,SubmissionUpdate 
from instructor.forms import ResourceUpdate
import datetime
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from course import models
from instructor.forms import ResourceForm


## @brief view for the index page of the student.
#
# This view is called by /index url.\n
# It returns the student's homepage containing links to all the courses he is enrolled in and all the notifications.
def home(request):
    return render(request,"course/home.html")


@login_required
def index(request):
    student = Student.objects.get(user=request.user)
    courses = student.course_list.all()
    notifications = Notification.objects.filter(course__in=courses)
    return render(request, 'course/index.html', {'courses': courses,'notifications': notifications})


## @brief view for the detail page of the course.
#
# This view is called by <course_id>/detail url.\n
# It returns the course's detail page containing forum and links to all the assignments and resources.
@login_required
def detail(request, course_id):
    user = request.user
    student = Student.objects.get(user=request.user)
    courses = student.course_list.all()
    course = Course.objects.get(id=course_id)
    instructor = course.instructor
    students = Student.objects.filter(course_list=course_id)
    messages = Message.objects.filter(course=course)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.course = course
            message.sender = user
            message.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y') # get the current date,time and convert into string
            message.save()
            students= Student.objects.filter(course_list=course_id)
            try:
                student = Student.objects.get(user=request.user)
                return redirect('course:detail', course_id)

            except:
                return redirect('instructor:instructor_detail', course.id)

    else:
        form = MessageForm()

        context = {
            'course': course,
            'user': user,
            'instructor': instructor,
            'student': student,
            'courses': courses,
            'messages': messages,
            'form': form,
            'students':students
        }

        return render(request, 'course/detail.html', context)


## @brief view for the assignments page of a course.
#
# This view is called by <course_id>/view_assignments url.\n
# It returns the webpage containing all the assignments of the course and links to download them and upload submissions.
@login_required
def view_assignments(request, course_id):
    course = Course.objects.get(id=course_id)
    assignments = Assignment.objects.filter(course=course)
    context = {
        'course' : course,
        'assignments' : assignments,
    }
    return render(request,'course/view_assignments.html',context)



## @brief view for the resources page of a course.
#
# This view is called by <course_id>/view_resources url.\n
# It returns the webpage containing all the resources of the course and links to download them.
@login_required
def view_resources(request, course_id):
    course = Course.objects.get(id=course_id)
    resources = Resources.objects.filter(course=course)
    context = {
        'course' : course,
        'resources' : resources,
    }
    return render(request,'course/view_resources.html',context)


## @brief view for the assignment's submission page.
#
# This view is called by <assignment_id>/upload_submission url.\n
# It returns the webpage containing a form to upload submission and redirects to the assignments page again after the form is submitted.


@login_required
def upload_submission(request, assignment_id):
    val= False
    feed= False
    form = SubmissionForm(request.POST or None, request.FILES or None)
    assignment = Assignment.objects.get(id=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)
    submission= Submission.objects.filter(user_id=request.user.id)
    for submissio in submission:
        if submissio.assignment_id == assignment.id:
            val=True
            break
    course_id = assignment.course.id
    course = Course.objects.get(id=course_id)
    feedbacks = Feedback.objects.filter(user_id=request.user.id)
    for submissio in submission:
        if submissio.assignment_id == assignment.id:
            for feedbac in feedbacks:
                if feedbac.submission_id == submissio.id:
                    feed=True
                    break
    if form.is_valid():
        submission = form.save(commit=False)
        submission.user = request.user
        submission.assignment = assignment
        submission.time_submitted = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        submission.save()
        return view_assignments(request, course_id)

    return render(request, 'course/upload_submission.html', {'form': form,'course': course,'submissions':submissions,'submission':submission,'assignment':assignment,'feedbacks':feedbacks,'val':val,'feed':feed})


def StudentsProfileUpdate(request,pk):
    profile_updated = False
    student = Student.objects.filter(user_id=request.user.id).first()
    if request.method == "POST":
        form = StudentprofileUpdate(request.POST,instance=student)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            profile_updated = True
            return render(request,"course/studentprofile.html",{'student':student})
    else:
        form = StudentprofileUpdate(request.POST or None,instance=student)
        return render(request,'course/student_update.html',{'profile_updated':profile_updated,'form':form,'student':student})


class StudentsDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "student"
    model = models.Student
    template_name = 'course/studentprofile.html'


def studentp(request,id):
    student=Student.objects.get(user_id=id)
    return render(request,"course/studentprofile.html",{'student':student})


def add_resources(request, course_id):
    form = ResourceForm(request.POST or None, request.FILES or None)
    course = Course.objects.get(id=course_id)
    student=Student.objects.get(user=request.user)
    if form.is_valid():
        resource = form.save(commit=False)
        resource.file_resource = request.FILES['file_resource']
        resource.course = course
        resource.user= request.user
        resource.save()
        notification = Notification()
        notification.content = "New Resource Added - " + resource.title
        notification.course = course
        notification.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        notification.save()
        return redirect('course:view_resources', course.id)

    return render(request, 'course/add_resources.html', {'form': form, 'course': course})




def editsubmission(request,submission_id,assignment_id=None):
    submission_updated = False
    submission= Submission.objects.get(id=submission_id)
    assignment = Assignment.objects.get(id=submission.assignment_id)
    course_id = assignment.course.id
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = SubmissionUpdate(request.POST,instance=submission)
        if form.is_valid():
            submission= form.save(commit=False)
            if 'file_submitted' in request.FILES:
                submission.file_submitted = request.FILES['file_submitted']
                submission.time_submitted = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
            #.course=course
            #resource.user = request.user
            submission.save()
            submission_updated = True
    else:
        form= SubmissionUpdate(request.POST or None,instance=submission)
    if submission_updated== True:
        return redirect('course:view_assignments',course_id)
    return render(request,'course/submissionupdate.html', {'submission_updated':submission_updated,'form':form,'submission':submission,'assignment':assignment,'course':course})


def editresources(request,resource_id,course_id=None):
    resource_updated = False
    resource= Resources.objects.get(id=resource_id)
    course_id = resource.course.id
    course = Course.objects.get(id=resource.course_id)
    if request.method == "POST":
        form = ResourceUpdate(request.POST,instance=resource)
        if form.is_valid():
            resource= form.save(commit=False)
            if 'file_resource' in request.FILES:
                resource.file_resource = request.FILES['file_resource']
            #.course=course
            #resource.user = request.user
            resource.save()
            resource_updated = True
            notification = Notification()
            notification.content = "Resource Updated - " + resource.title
            notification.course = course
            notification.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
            notification.save()
    else:
        form= ResourceUpdate(request.POST or None,instance=resource)
    if resource_updated == True:
        return redirect('course:view_resources',course_id)
    return render(request,'course/resourceupdate.html', {'resource_updated':resource_updated,'form':form,'resource':resource,'course':course})


