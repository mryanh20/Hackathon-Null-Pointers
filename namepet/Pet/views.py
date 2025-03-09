from django.shortcuts import render
from .models import Adoptee
from django.http import HttpResponse

# Create your views here.
def list_unnamed(request):
    adoptees = Adoptee.objects.filter(name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

def list_cats(request):
    adoptees = Adoptee.objects.filter(species="Cat", name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

def list_dogs(request):
    print(request.GET.get('breed'))
    adoptees = Adoptee.objects.filter(species="Dog", name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

