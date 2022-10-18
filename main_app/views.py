from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Aftermarket
from .forms import OilChangeForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def aftermarket_index(request):
    aftermarket = Aftermarket.objects.all()
    return render(request, 'aftermarket/index.html', {'aftermarket': aftermarket})

@login_required
@login_required
def cars_create(request):
    return render(request, 'cars/car_form.html')

@login_required
def aftermarket_create(request):
    return render(request, 'aftermarket/aftermarket_form.html')

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    oilchange_form = OilChangeForm()
    aftermarket_car_doesnt_have = Aftermarket.objects.exclude(id__in=car.aftermarket.all().values_list('id'))
    return render(request, 'cars/detail.html', {
        'car': car, 
        'oilchange_form': oilchange_form, 
        'aftermarket': aftermarket_car_doesnt_have
        })

@login_required
def aftermarket_detail(request, aftermarket_id):
    aftermarket = Aftermarket.objects.get(id=aftermarket_id)
    return render(request, 'aftermarket/detail.html', {
        'aftermarket': aftermarket
    })

@login_required
def add_oilchange(request, car_id):
    print(request.POST)
    form = OilChangeForm(request.POST)
    if form.is_valid():
        new_oilchange = form.save(commit=False)
        new_oilchange.car_id = car_id
        new_oilchange.save()
    else:
        print(form.errors)
    return redirect('cars_detail', car_id=car_id)

@login_required
def assoc_aftermarket(request, car_id, aftermarket_id):
    Car.objects.get(id=car_id).aftermarket.add(aftermarket_id)
    return redirect('cars_detail', car_id=car_id)

@login_required
def del_aftermarket(request, car_id, aftermarket_id):
    Car.objects.get(id=car_id).aftermarket.remove(aftermarket_id)
    return redirect('cars_detail', car_id=car_id)

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cars_index')
        else:
            error_message = 'Signup Input Invalid - Please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class AftermarketIndex(LoginRequiredMixin, ListView):
    template_name = 'aftermarket/index.html'
    model = Aftermarket

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ('make', 'model', 'year', 'color', 'trim')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AftermarketCreate(LoginRequiredMixin, CreateView):
    model = Aftermarket
    fields = '__all__'

class AftermarketDetail(LoginRequiredMixin, DetailView):
    template_name = 'aftermarket/detail.html'
    model = Aftermarket

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['model', 'year', 'color', 'trim']

class AftermarketUpdate(LoginRequiredMixin, UpdateView):
    model = Aftermarket
    fields = ['material', 'type']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

class AftermarketDelete(LoginRequiredMixin, DeleteView):
    model = Aftermarket
    success_url = '/aftermarket/'