from django.shortcuts import render
from MiApp.models import Family

# Create your views here.

def showFamily(request):

   f1 = Family(name = 'Eduardo', lastName = 'Goldenhorn', age = 59)
   f2 = Family(name = 'Gabriela', lastName = 'Ferrandez', age = 59)

   return render(request, 'MiApp/family.html' ,{'family':[f1, f2]})

