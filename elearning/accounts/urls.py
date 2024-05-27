# accounts/urls.py
from django.urls import path
from .views import StudentRegistrationView, TutorRegistrationView, user_login, user_logout

urlpatterns = [
    path('student/register/', StudentRegistrationView, name='student-register'),
    path('tutor/register/', TutorRegistrationView, name='tutor-register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
