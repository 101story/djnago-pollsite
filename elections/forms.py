
from django import forms
from .models import Candidate, Poll, Choice


class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'introduction','area','party_number')
