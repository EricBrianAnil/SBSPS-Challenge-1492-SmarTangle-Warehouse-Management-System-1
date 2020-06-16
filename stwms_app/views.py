from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .forms import SignUpForm
from .models import StoreDetails, StoreInventory

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
    stores_data = StoreDetails.objects.all()
    context = {'stores': stores_data, 'storesLen': len(stores_data)}
    return render(request, 'stores.html', context)


def store_details(request):
    if request.method == "GET":
        store_id = request.GET['store_id']
        items_data = StoreInventory.objects.filter(storeId=store_id)
        store_data = StoreDetails.objects.get(store_id=store_id)
        context = {'items': items_data, 'store': store_data}
        return render(request, 'storeDetails.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
