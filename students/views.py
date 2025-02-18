from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def home_view(request):
    """
    Redirect user to a role-specific dashboard.
    """
    user = request.user
    if user.is_admin():
        return redirect('admin_page')
    elif user.is_teacher():
        return redirect('teacher_page')
    elif user.is_student():
        return redirect('student_page')
    return render(request, 'home.html')
@login_required
def admin_page(request):
    return render(request, 'admin_page.html')
@login_required
def teacher_page(request):
    return render(request, 'teacher_page.html')
@login_required
def student_page(request):
    return render(request, 'student_page.html')













