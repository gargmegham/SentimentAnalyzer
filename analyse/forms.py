from django import forms

class userinput(forms.Form):
    q=forms.CharField(required=True)
