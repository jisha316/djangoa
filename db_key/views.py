
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import course,student

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')


def loginpage(request):
    return render(request,'login.html')  

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

# @login_required(login_url='login')
def course_page(request):
    return render(request,'add_course.html')

# @login_required(login_url='login')
def student_page(request):
    courses = course.objects.all()
    context={'courses':courses}
    return render(request,'add_student.html',context) 

def show(request):
    std=student.objects.all()
    return render(request,'show.html',{'student':std})


def logout_page(request):
    return render(request,'logout.html')

#......Msg Passing and Check Username and Password....
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Welcome {username}')
			return redirect('about')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		return redirect('loginpage')

#User logout functionality view
@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('home')

# @login_required(login_url='login')
def add_course(request):
    if request.method=='POST':
        cname=request.POST['course_name']
        cfee=request.POST['fee']
        crs=course(course_name=cname,
                    fee=cfee)
        # cors=request.POST['course_name']
        # cfe=request.POST['fee']
        # print(cors)
        # crs=course()      
        # crs.course_name=cors
        # crs.fee=cfe
        crs.save()
        print("haii")
        return redirect('student_page')

# @login_required(login_url='login')
def add_student(request):
    if request.method=='POST':
        sname=request.POST['name']
        adrs=request.POST['address']
        mail=request.POST['email']
        ag=request.POST['age']
        jdt=request.POST['join_date']
        sc=request.POST['slct']
        course1=course.objects.get(id=sc)
        std=student(name=sname,
                    address=adrs,
                    email=mail,
                    age=ag,
                    join_date=jdt,
                    course=course1)
        std.save()
        print("haiii")
        return redirect('show')
    return render(request,'add_student.html')
    
