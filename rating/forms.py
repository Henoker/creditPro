from django import forms
from .models import CreditRating, Sector

class CreditRatingForm(forms.ModelForm):
    class Meta:
        model = CreditRating
        fields = [
            'user',
            'maker',
            'checker',
            'staff',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # widgets, labels, or other customizations I should add here later
