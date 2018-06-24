from django import forms
class gallaryVideoForm(forms.Form):
    content = forms.ImageField(required=True)
    style = forms.ImageField(required=True)
