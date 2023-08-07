from django import forms

class AgeForm(forms.Form):#this is a simple example form only to take two parameters in input
    name = forms.CharField(label='Your name',max_length=100)
    age = forms.IntegerField(label='How old are you?',max_value=150)
    info = forms.CharField(label='Give us some extra information',widget=forms.Textarea())
    #the django forms already gives some instruction to the html