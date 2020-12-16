from django.shortcuts import render
from django.http import HttpResponse


class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Tex','golden retreiver', 'super active', 3),
  Dog('Fido', 'dachsund', 'very long', 0),
  Dog('Rover', 'chihuahua', '3 legged dog', 4)
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')
def dogs_index(request):
  return render(request, 'dogs/index.html', { 
    'dogs': dogs 
  })