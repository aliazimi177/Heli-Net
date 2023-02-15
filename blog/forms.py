from .models import Commnt
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commnt
        fields = ("name","email","body")

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()

        
    
