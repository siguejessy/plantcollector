from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Holder
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html',
  {
    'plants': plants
  })

def plants_detail(request, plant_id):
   plant = Plant.objects.get(id=plant_id)
   id_list = plant.holders.all().values_list('id')
   holders_plant_doest_have = Plant.objects.exclude(id__in=id_list)
   feeding_form = FeedingForm()
   return render(request, 'plants/detail.html', {
      'plant': plant, 'feeding_form': feeding_form, 'holders': holders_plant_doest_have
    })

class PlantCreate(CreateView):
  model = Plant
  fields = ['common_names', 'description', 'acquired_via']

class PlantUpdate(UpdateView):
   model = Plant
   fields = '__all__'

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

def add_feeding(request, plant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.plant_id = plant_id
    new_feeding.save()
  return redirect('detail', plant_id=plant_id)

class HolderList(ListView):
  model = Holder

class HolderDetail(DetailView):
  model = Holder

class HolderCreate(CreateView):
  model = Holder
  fields = '__all__'

class HolderUpdate(UpdateView):
  model = Holder
  fields = ['name', 'type', 'description']

class HolderDelete(DeleteView):
  model = Holder
  success_url = '/holders'

def assoc_holder(request, plant_id, holder_id):
  Plant.objects.get(id=plant_id).holders.add(holder_id)
  return redirect('detail', plant_id=plant_id)


def unassoc_holder(request, plant_id, holder_id):
  Plant.objects.get(id=plant_id).holders.remove(holder_id)
  return redirect('detail', plant_id=plant_id)