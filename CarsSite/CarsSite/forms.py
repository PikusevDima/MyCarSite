from django import forms
from .models import Brand, Person


class UserName(forms.Form):
    person_name = forms.CharField(label="Имя пользователя", max_length=20)


class BrandName(forms.Form):
    brand_name = forms.CharField(label="Название марки", max_length=31)


class CarManufacturerName(forms.Form):
    CarManufacturer_Name = forms.CharField(label="Название производителя", max_length=31)


class CarNew(forms.Form):
    brand = forms.ModelChoiceField(widget=forms.Select,
                                   queryset=Brand.objects.all())
    users = forms.ModelChoiceField(widget=forms.Select,
                                   queryset=Person.objects.all())
