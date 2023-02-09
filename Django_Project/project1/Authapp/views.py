from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate,login, logout

# Create your views here.

class register_view(View):
    def get(self, request):
        form = UserCreationForm()
        template_name = 'Authapp/register.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        template_name = 'Authapp/register.html'
        context = {'form': form}
        return render(request, template_name, context)


class login_view(View):
    def get(self, request):

        template_name = 'Authapp/login.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        if request.method == 'POST':
            u = request.POST["un"]
            p = request.POST["pw"]
            user = authenticate(username=u, password=p)
            if user is not None:
                login(request, user)
                return redirect('show_url')
        template_name = 'Authapp/login.html'
        context = {}
        return render(request, template_name, context)


class logout_view(View):
    def get(self, request):
        logout(request)
