from django import forms

class PetForm(forms.Form):
    animal_name = forms.CharField(label="Animal name", max_length=100)
    animal_id = forms.IntegerField(label="Animal ID")