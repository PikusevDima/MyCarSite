from django import forms


class PersonName(forms.Form):
    person_name = forms.CharField(label="Person name", max_length=20)
