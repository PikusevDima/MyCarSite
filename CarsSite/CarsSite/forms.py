from django import forms


class UserName(forms.Form):
    person_name = forms.CharField(label="Person name", max_length=20)
