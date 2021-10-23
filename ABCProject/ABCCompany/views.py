from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import UserRegistration
from .forms import NewUserForm
from .forms import NumWordForm
from .forms import EmpLoginForm
from num2words import num2words
import gtts
from playsound import playsound


def home(request):
    employees = UserRegistration.objects.filter(is_employee=True)
    ceos = UserRegistration.objects.filter(is_superuser=True)
    return render(request=request, template_name="home.html", context={"employees": employees, "ceos": ceos})


@login_required(login_url='/admin-login/')
def register(request):
    if request.method == "POST":

        form = NewUserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data.get('email'))
            user = form.save()
            return redirect('/')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="register.html",
                          context={"form": form})
    form = NewUserForm

    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


def login_view(request):
    print("inside login")
    if request.method == 'POST':
        print("if")
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    print("2")
    form = AuthenticationForm()
    context = {"form": form}
    print(context)
    return render(request=request,
                  template_name="admin_login.html",
                  context=context)


@csrf_exempt
def emp_login_view(request):
    print("inside login")
    form = EmpLoginForm()

    if request.method == 'POST':
        print("if")
        # form = EmpLoginForm(request=request, data=request.POST)
        # if form.is_valid():
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user_data = UserRegistration.objects.get(email=email)
        user = authenticate(username=user_data.username, password=password)
        print("user", user)
        if user is not None:
            print("1")
            login(request, user)
            messages.info(request, f"You are now logged in as {email}")
            print(request.user)
            return redirect('/')
        else:
            print("2")
            messages.error(request, "Invalid email or password.")
        # else:
        #     print("3")
        #     messages.error(request, "Invalid email or password.")
    print("2")
    form = EmpLoginForm()
    context = {"form": form}
    print(context)
    return render(request=request,
                  template_name="emp_login.html",
                  context=context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def individual_employee(request, id):
    # query = Posts.objects.get(id=id)
    liked = False
    query = get_object_or_404(UserRegistration, id=id)

    return render(request, 'emp_details.html', {"user": request.user, "query": query})


@login_required
def delete_employee(request, id):
    user = request.user

    instance = UserRegistration.objects.get(id=id)
    if instance.id == user.id:
        print(instance.id)

        if instance:
            instance.delete()
        return redirect("/")
    else:
        return redirect("/")


def num_to_word(request):
    form = NumWordForm(request.POST or None)
    print(request.POST)
    word = 'Please type your number'
    if form.is_valid():
        number = form.cleaned_data.get('number')
        print(number)
        word = num2words(number, to='cardinal')
        print(word)
    else:
        print("else")
    tts = gtts.gTTS(word)
    tts.save("hello.mp3")
    playsound("hello.mp3")
    context = {"form": form, "word": word}
    return render(request, 'num_to_word.html', context=context)
