from django.shortcuts import render, redirect

from main.models import LoginForm, SignupForm


def index(request):
    return render(request, 'index.html', {})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            token = login_form.login()

            if token:
                request.session['token'] = token
                return redirect('/dashboard')
            else:
                return render(request, 'index.html', {'login_error': True})


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            if signup_form.signup():
                return render(request, 'index.html', {'signup_success': True})
            else:
                return render(request, 'index.html', {'signup_error': True})
