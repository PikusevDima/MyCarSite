from django import forms


class UserName(forms.Form):
    person_name = forms.CharField(label="User name", max_length=20)
