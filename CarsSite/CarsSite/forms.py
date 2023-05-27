from django import forms
from .models import Brand, Person, Car


class UserName(forms.Form):
    person_name = forms.CharField(label="Имя пользователя", max_length=20)


class BrandName(forms.Form):
    brand_name = forms.CharField(label="Название марки", max_length=31)
    carManufacturer_Name = forms.CharField(label="Название производителя", max_length=31)

class CarNew(forms.Form):
    brand_id = forms.ModelChoiceField(widget=forms.Select,
                                      queryset=Brand.objects.all())
    users = forms.ModelChoiceField(widget=forms.Select,
                                   queryset=Person.objects.all())
    image = forms.CharField(label="Image", max_length=401)
    cost = forms.CharField(label="Cost", max_length=12)
    speed = forms.CharField(label="Speed", max_length=4)
    name = forms.CharField(label="Name", max_length=31)
