from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm
from accounts.models import User

# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


@login_required
def IndexPage(request):
    return render(request, 'index.html')
