from django.shortcuts import render

plants = [
    {'common_name': 'ZZ Plant', 'botanical_name': 'Zamioculcas zamiifolia', 'sunlight': 'Partial', 'water': 'when soil is bone dry', 'leaves': 'Green, shiny'},
    {'common_name': 'Monstera', 'botanical_name': 'Monstera acacoyaguensis', 'sunlight': 'Bright and Indirect', 'water': 'when top of soil is dry', 'leaves': 'Green, shiny'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', {
    'plants': plants
  })