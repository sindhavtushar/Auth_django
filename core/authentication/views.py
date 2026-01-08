import datetime
import math
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from authentication.helper import Calculator

calc = Calculator()


# Create your views here.

@login_required(login_url='/login/')
def home(request):
    return render(request, "authentication/home.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    return render(request, 'authentication/login.html')
    # return render(request, 'authentication/home.html')
    # return render(request, 'authentication/register.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username Already Taken!")
            return redirect('/register/')
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name, 
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/login/')
    
    return render(request, 'authentication/register.html')


def simple_calculator(request):
    res = None

    if request.method == "POST":
        oprdL = request.POST.get('oprdL')
        oprtr = request.POST.get('oprtr')
        oprdR = request.POST.get('oprdR')

        # Optional: check if inputs are valid numbers
        try:
            res = calc.simple_calc(oprdL, oprdR, oprtr)
            messages.success(request, "Calculated Successfully!")
        except Exception as e:
            res = None
            messages.error(request, f"Error: {e}")
            return redirect('/simple_calculator/')

    return render(request, 'authentication/simple_calculator.html', {'res': res})



def scientific_calculator(request):
    result = ''
    expression = ''
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # safe evaluation
            result = eval(expression, {"__builtins__": None, "sqrt": math.sqrt,
                                       "sin": math.sin, "cos": math.cos,
                                       "tan": math.tan, "pi": math.pi})
        except Exception as e:
            result = 'Error'

    return render(request, 'authentication/scientific_calculator.html', {'result': result, 'expression': expression})


def percentage_calculator(request):
    res = None
    
    if request.method == 'POST':
            
        part = request.POST.get('part')
        whole = request.POST.get('whole')
        try:
            part, whole = float(part), float(whole)
            res = calc.percentage_calc(part, whole)
            # print(f'[DEBUG]: {res}')    
        except Exception as e:
            messages.error(request, f"problem while calculating: {e}")
            return redirect('/percentage_calculator/')
    return render(request, 'authentication/percentage_calculator.html', {'result': res})

def age_calculator(request):
    age = None

    if request.method == 'POST':
        start_date = request.POST.get('init_date')
        end_date = request.POST.get('end_date')

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print(f'[DEBUG]: {start_date} to {end_date}', type(start_date), type(end_date))
        
        age = calc.age_calc(start_date, end_date)
        print(age)

    return render(request, 'authentication/age_calculator.html', {'result': age})

def table_generator(request):
    table = None
    if request.method == "POST":
        n = int(request.POST.get('num'))

        try:
            table = [(n, i, n*i) for i in range(1,11)]  
        except Exception as e:
            table = None
            messages.error(request, f'Error: {e}')
            return redirect('/table_generator/')
        
    return render(request, 'authentication/table_generator.html', {'table': table})
    

        