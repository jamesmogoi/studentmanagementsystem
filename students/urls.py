from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    home_view,
    admin_page,
    teacher_page,
    student_page,
)
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('admin/', admin_page, name='admin_page'),
    path('teacher/', teacher_page, name='teacher_page'),
    path('student/', student_page, name='student_page'),
]









