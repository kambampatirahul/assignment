from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from .models import student, assignment
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        id = request.POST['id']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        catageory = request.POST['catageory']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(password=password1, username=email, first_name=firstname, id=id,
                                                last_name=lastname)
                user.save()
                stu = student()
                stu.name = firstname
                stu.st_id = id
                stu.catageory = catageory
                stu.email = email
                stu.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('email')
        password = request.POST.get('password')
        catageory = request.POST.get('catageory')
        cat = student.objects.get(email=user_name)
        print(cat)
        if cat.catageory == catageory:
            user = authenticate(username=user_name, password=password)
        else:
            messages.info(request, 'invalid catageory')
            return redirect('login')
        if user is not None:
            auth.login(request, user)
            if catageory == 'student':
                return redirect('showassignment')
            else:
                return redirect('assignments')
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


def addassignment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['assignment title']
            questions = request.POST['questions']
            deadline = request.POST['deadline']
            id = request.POST['id']
            ass = assignment()
            #print(id)
            ass.te_id = request.user.id
            ass.stu = student.objects.get(st_id=id)
            ass.title = title
            ass.questions = questions
            ass.deadline = deadline
            ass.save()
            messages.info(request, 'assignment sent succesfully')
            return redirect('assignments')
        else:
            return render(request, 'addassignment.html')
    else:
        return render(request, 'login.html')


def showassignment(request):
    if request.user.is_authenticated:
        id = request.user.id
        sa = assignment.objects.filter(stu_id=id)
        now = datetime.date.today()
        return render(request, 'showassignment.html', {'sa': sa, 'now': now})
    else:
        return render(request, 'login.html')


def solassignment(request, title):
    #print(title)
    if request.user.is_authenticated:
        ass = assignment.objects.get(title=title)
        print(ass)
        return render(request, 'solassignment.html', {'ass': ass})
    else:
        return render(request, 'login.html')


def ass(request,title):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sol = request.POST['solution']
            assignment.objects.filter(stu_id=request.user.id, title=title).update(solution=sol)
            return redirect('showassignment')

def assignments(request):
    if request.user.is_authenticated:
        id = request.user.id
        sa = assignment.objects.filter(te_id=id)
        return render(request, 'assignments.html', {'sa': sa})

def rewords(request,title,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            marks = request.POST['marks']
            remarks = request.POST['remarks']
            assignment.objects.filter(stu_id=id, title=title).update(marks=marks, remarks=remarks)
            return redirect('assignments')
        else:
            ass = assignment.objects.get(title=title)
            return render(request, 'rewords.html', {'ass': ass})