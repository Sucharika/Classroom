from django.urls import include, path 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

## @brief url patterns for the website.
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('course.urls')),
    path('login/', views.login_user, name='login_user'),
    path('login_stud/', views.login_stud, name='login_stud'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('course/', include(('course.urls', 'course'), namespace='course')),
    path('instructor/', include(('instructor.urls', 'instructor'), namespace='instructor')),
   
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

