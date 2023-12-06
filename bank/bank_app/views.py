from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . models import UserDetails

# Create your views here.
def home(request):
    return render(request, 'home.html')
def single(request):
    return render(request, 'single_blog.html')
def go_to_registration_form(request):
    u_user = request.user
    u_name = u_user.username
    data = UserDetails.objects.filter(user_name=u_name)
    return render(request,'go_to_registration.html',{'data':data})
def registration_form(request):

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        ac = request.POST['ac']
        debit_card = request.POST.get('debit_card', False);
        credit_card = request.POST.get('credit_card', False);
        cheque_book = request.POST.get('cheque_book', False);

        u_user = request.user
        u_name = u_user.username
        print(u_name)

        if name == "" or dob == "" or age == "" or gender == "" or phone == "" or email == "" or address == "" or district == "" or branch == "" or ac == "" or debit_card == "" or credit_card == "" or cheque_book == "":
            messages.info(request, "Please fill all datas")
            return redirect('registration_form')
        else:
            print(u_name, name, dob, age, gender, phone, email, address, district, branch, ac, debit_card, credit_card, cheque_book)

            data = UserDetails (user_name=u_name, name=name, dob=dob, age=age, gender=gender, phone=phone, email=email, address=address, district=district, branch=branch, account=ac, debit_card=debit_card, credit_card=credit_card, cheque_book=cheque_book)
            data.save()
            messages.info(request, "application accepted successfully")
            return redirect('go_to_registration_form')

    return render(request, 'registration_form.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('go_to_registration_form')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['pass']
        cpassword1 = request.POST['cpass']
        if username1 == "" or password1 == "" or cpassword1 == "":
            messages.info(request, "Please fill all datas")
            return redirect('register')
        else:
            if password1 == cpassword1:
                if User.objects.filter(username=username1).exists():
                    messages.info(request, "Username Taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username1, password=password1)
                    user.save()
                    print("user created")
                    messages.info(request, "user created")
                    return redirect('login')
            else:
                print("password not same")
                messages.info(request, "password not same")
                return redirect('register')

    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
