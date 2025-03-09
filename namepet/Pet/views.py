from django.shortcuts import render
from .models import Adoptee
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def list_unnamed(request):
    adoptees = Adoptee.objects.filter(name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

def list_cats(request):
    adoptees = Adoptee.objects.filter(species="Cat", name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

def list_dogs(request):
    adoptees = Adoptee.objects.filter(species="Dog", name__isnull=True)
    return render(request, "list.html", {"adoptees": adoptees})

def json_unnamed(request):
    adoptees = list(Adoptee.objects.filter(name__isnull=True).values())
    return JsonResponse(adoptees, safe=False)

def json_cats(request):
    adoptees = list(Adoptee.objects.filter(species="Cat", name__isnull=True).values())
    return JsonResponse(adoptees, safe=False)

def json_dogs(request):
    adoptees = list(Adoptee.objects.filter(species="Dog", name__isnull=True).values())
    return JsonResponse(adoptees, safe=False)



