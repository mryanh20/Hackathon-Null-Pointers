from django.shortcuts import render
from .models import Adoptee
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import PetForm

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

def get_name(request):
    adoptees = Adoptee.objects.filter(name__isnull=True)
    pet_form = PetForm(request.POST)
    if request.method == 'POST':
        if pet_form.is_valid():
            animal_name = pet_form.cleaned_data["animal_name"]
            animal_id = pet_form.cleaned_data["animal_id"]
            pet = Adoptee.objects.filter(id=animal_id).first()
            print(pet)
            if pet:
                if not pet.name:
                    print(pet)
                    pet.name = animal_name
                    pet.save()
                    return render(request, "success.html")
                else:
                    print("Pet already has a name.")
    else:
        form = PetForm()
    return render(request, "name.html", {"pet_form": pet_form, "adoptees": adoptees})






