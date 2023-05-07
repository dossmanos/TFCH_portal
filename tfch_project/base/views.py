from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from .models import User, Program, Composition, Pianist, Concert
from .forms import UserForm, MyUserCreationForm, ProgramForm, ConcertForm
import datetime, calendar

# Create your views here.


def error(request, error_message: str):
    context = {"message": error_message}
    return render(request, "base/error.html", context)
    # return render(request,'base/error.html',{'message':"........your message here......"})
    # sample code to inform user about something


def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home page")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Specified user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home page")
        else:
            messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło")

    context = {"page": page}
    return render(request, "base/login_form.html", context)


def logout_page(request):
    logout(request)
    return redirect("home page")


def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home page")
        else:
            messages.error(request, "registration failed")

    return render(request, "base/login_form.html", {"form": form})


def home_page(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    # list_of_concerts = Concert.objects.filter(
    #     Q(concert_pianist__icontains=q) |
    #     Q(concert_date__icontains=q) |
    #     Q(concert_program__icontains=q)
    current_time = datetime.date.today().strftime("%d %b %Y, %a")
    pianists = Pianist.objects.all()
    programs = Program.objects.all()
    concerts = Concert.objects.all()
    precise_time = datetime.datetime.now()
    months = calendar.month_name
    c = calendar.TextCalendar(calendar.SUNDAY)

    context = {
        "concerts": concerts,
        "programs": programs,
        "time": current_time,
        "pianists": pianists,
        "precise_time": precise_time,
        "calendar": c,
        "months": months,
    }
    return render(request, "base/home.html", context)


@login_required(login_url="login")
def create_a_program(request):
    program_form = ProgramForm()
    user = request.user
    pianist = user.pianist
    if request.method == "POST":
        try:
            Program.objects.create(
                program_pianist=request.user,
                name=request.POST.get("name"),
            )
            created_program = Program.objects.get(name=request.POST.get("name"))
            pianist.programs.add(created_program)
            primary_key = created_program.id
            return redirect("program", primary_key)
        except:
            return render(
                request,
                "base/error.html",
                {"message": "Nazwa programu nie może się powtarzać"},
            )
    context = {"form": program_form}
    return render(request, "base/new_program_form.html", context)


@login_required(login_url="login")
def create_a_concert(request):
    concert_form = ConcertForm()
    user = request.user
    users = User.objects.all()
    programs = Program.objects.all()
    pianists = Pianist.objects.all()
    time = datetime.datetime.now()
    if request.method == "POST":
        if user.is_superuser == False:
            return render(
                request,
                "base/error.html",
                {"message": "Brak uprawnień do tworzenia koncertów"},
            )
        else:
            try:
                Concert.objects.create(
                    concert_pianist=Program.objects.get(
                        id=request.POST.get("concert_program")
                    ).program_pianist,
                    concert_program=Program.objects.get(
                        id=request.POST.get("concert_program")
                    ),
                    concert_date=request.POST.get("concert_date"),
                )
                created_concert = Concert.objects.get(
                    concert_date=request.POST.get("concert_date")
                )
                primary_key = created_concert.id
                return redirect("concert", primary_key)
            except:
                return render(
                    request,
                    "base/error.html",
                    {"message": "W bazie jest już koncert z identyczną datą"},
                )

    context = {
        "form": concert_form,
        "programs": programs,
        "time": time,
        "users": users,
        "pianists": pianists,
    }
    return render(request, "base/new_concert_form.html", context)


@login_required(login_url="login")
def program(request, primary_key):
    program = Program.objects.get(id=primary_key)
    compositions = program.compositions.all()
    if request.method == "POST":
        program.delete()
        return redirect("home page")

    context = {"program": program, "compositions": compositions}
    return render(request, "base/program.html", context)


@login_required(login_url="login")
def concert(request, primary_key):
    concert = Concert.objects.get(id=primary_key)
    program = concert.concert_program.compositions.all()
    date = concert.concert_date
    if request.method == "POST":
        concert.delete()
        return redirect("home page")

    context = {"concert": concert, "date": date, "program": program}
    return render(request, "base/concert.html", context)


@login_required(login_url="login")
def modify_program(request, primary_key):
    program = Program.objects.get(id=primary_key)
    compositions = program.compositions.all()
    all_compositions = Composition.objects.all()
    if request.method == "POST":
        try:
            if "add" in request.POST:
                program.compositions.add(request.POST.get("composition"))
            elif "remove" in request.POST:
                program.compositions.remove(request.POST.get("composition"))
            elif "remove all" in request.POST:
                program.compositions.clear()
        except:
            return render(
                request,
                "base/error.html",
                {
                    "message": "Nie wybrano kompozycji. Spróbuj ponownie wybierając jakąś kompozycję z listy"
                },
            )

    context = {
        "program": program,
        "primary_key": program.id,
        "compositions": compositions,
        "all_compositions": all_compositions,
    }
    return render(request, "base/modify_program.html", context)


@login_required(login_url="login")
def modify_concert(request, primary_key):
    concert = Concert.objects.get(id=primary_key)
    pianist = concert.concert_pianist.get_full_name()
    program = concert.concert_program
    program_compositions = concert.concert_program.compositions.all()
    date = concert.concert_date
    users = User.objects.all()
    programs = Program.objects.all()
    pianists = Pianist.objects.all()
    concerts = Concert.objects.all()
    if request.method == "POST":
        if request.user.is_superuser == False:
            return render(
                request,
                "base/error.html",
                {"message": "Brak uprawnień do modyfikacji koncertów"},
            )
        else:
            # try:
            Concert.objects.filter(id=primary_key).update(
                concert_pianist=Program.objects.get(
                    id=request.POST.get("concert_program")
                ).program_pianist.id,
                concert_program=Program.objects.get(
                    id=request.POST.get("concert_program")
                ),
            )
            primary_key = concert.id
            return redirect("concert", primary_key)
        # except:
        # return render(request,'base/error.html',{'message':"W bazie jest już koncert z identyczną datą"})

    if request.method == "POST":
        try:
            if "add" in request.POST:
                program.compositions.add(request.POST.get("composition"))
            elif "remove" in request.POST:
                program.compositions.remove(request.POST.get("composition"))
            elif "remove all" in request.POST:
                program.compositions.clear()
        except:
            return render(
                request,
                "base/error.html",
                {
                    "message": "Nie wybrano kompozycji. Spróbuj ponownie wybierając jakąś kompozycję z listy"
                },
            )

    context = {
        "concert": concert,
        "primary_key": concert.id,
        "program": program,
        "pianist": pianist,
        "date": date,
        "program_compositions": program_compositions,
        "users": users,
        "pianists": pianists,
        "programs": programs,
    }
    return render(request, "base/modify_concert.html", context)


@login_required(login_url="login")
def user_profile(request, primary_key):
    user = User.objects.get(id=primary_key)
    programs = Program.objects.filter(program_pianist=user)

    context = {
        "user": user,
        "programs": programs,
    }
    return render(request, "base/user_profile.html", context)


@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user profile", primary_key=user.id)

    return render(request, "base/update_user.html", {"form": form})
