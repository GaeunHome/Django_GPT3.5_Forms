from django import forms

class infoForm(forms.Form): 
    name = forms.CharField(max_length=20) 
    descriptions = forms.CharField(widget=forms.Textarea)