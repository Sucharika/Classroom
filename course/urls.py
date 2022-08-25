## @brief urls for the course app.

from django.urls import include, path,re_path
from django.contrib import admin
from . import views

## @brief url patterns for the course app.
urlpatterns = [
    path('',views.home,name="home"),
    re_path(r'^$', views.index),
    re_path(r'^(?P<course_id>[0-9]+)/detail/$', views.detail, name='detail'),
    re_path(r'^index/$', views.index, name='index'),

    re_path(r'^(?P<assignment_id>[0-9]+)/upload_submission/$', views.upload_submission, name='upload_submission'),
    re_path(r'^(?P<assignment_id>[0-9]+)/upload_submission/(?P<submission_id>[0-9]+)$', views.editsubmission, name='submissionupdate'),
    re_path(r'upload_submission/(?P<submission_id>[0-9]+)$', views.editsubmission, name='submissionupdate'),
    re_path(r'^(?P<course_id>[0-9]+)/upload_submission/course/view_assignments/$', views.view_assignments, name='view_assignments'),
     

    re_path(r'^(?P<course_id>[0-9]+)/view_assignments/$', views.view_assignments, name='view_assignments'),
    re_path(r'^(?P<course_id>[0-9]+)/view_resources/$', views.view_resources, name='view_resources'),
    #path('student/<int:pk>/',views.StudentsDetailView.as_view(),name="studentprofile"),
    path('student/<int:id>/',views.studentp,name="studentprofile"),
    path('update/course/<int:pk>/',views.StudentsProfileUpdate,name="student_update"),
    re_path('^(?P<course_id>[0-9]+)/add_resources/$', views.add_resources, name='add_resources'),
    
    re_path(r'^(?P<course_id>[0-9]+)/view_resources/(?P<resource_id>[0-9]+)$', views.editresources, name='editresources'),
    re_path(r'view_resources/(?P<resource_id>[0-9]+)$', views.editresources, name='editresources'),
    re_path(r'^(?P<course_id>[0-9]+)/view_resources/course/view_resources/$', views.view_resources, name='view_resources')
]