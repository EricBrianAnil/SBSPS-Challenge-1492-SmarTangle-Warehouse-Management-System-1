from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .forms import SignUpForm
from .models import StoreDetails

# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html')


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home.html')
    context['form'] = form
    return render(request, 'sign_up.html', context)


def index(request):
    return render(request, 'index.html')


def stores(request):

    return render(request, 'stores.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
