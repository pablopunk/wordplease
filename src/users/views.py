from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import SignUpForm

pagination = 7


def blogs(request):
    page = request.GET.get('page')
    if page is None:
        page = 0
    page = int(page)

    from_n = pagination * page
    to_n = from_n + pagination
    users = User.objects.all()
    usersCount = users.count()

    previousPage = page - 1
    nextPage = page + 1

    if nextPage * pagination > (usersCount - 1):
        nextPage = -1

    ctx = {
        'blogs': users[from_n:to_n],
        'page': page,
        'previousPage': str(previousPage),
        'nextPage': str(nextPage),
    }

    return render(request, "blogs.html", ctx)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})
