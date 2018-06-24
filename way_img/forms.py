from django import forms
class gallaryImgForm(forms.Form):
    content = forms.ImageField(required=True)
