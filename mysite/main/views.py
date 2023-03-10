from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url
from django.views.generic import CreateView
from main.models import CustomUser,Gender 

# Create your views here.
def index(request):
    print("HELLO")

    return render(request, 'main/index.html')

def login(request):
    print("HELLO")

    return render(request, 'main/login.html')
def registration(request):
    print("HELLO")

    return render(request, 'main/registration.html')

def news(request):
    print("HELLO")

    return render(request, 'main/news.html')


class CustomLoginView(LoginView):
    template_name='main/login.html'

    def get_success_url(self):
        return resolve_url('index')


class CustomRegistrationView(CreateView):
    template_name = 'main/registration.html'
    model = CustomUser

    def get(self, request):
        return render(request, 'main/registration.html')

    def post(self, request):
        new_user = CustomUser()
        password = ""
        print("vadim")

        if request.POST.get("password1") != request.POST.get("password2"):
            return render(request, "main/registration.html")
        else:
            password = request.POST.get("password1")
        
        print(request.POST.get("gender"))
        gender = Gender.objects.get(id=request.POST.get("gender"))
        print(gender)
        CustomUser.objects.create_user(
            username = request.POST.get("username"),
            password = password,
            email = request.POST.get("email"),
            age = request.POST.get("age"),
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            gender =gender, 
            phone_number = request.POST.get("phone_number"),
        )

        return render(request, "main/registration_success.html")
