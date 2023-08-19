from django import forms
from .models import CreditRating

class CreditRatingForm(forms.ModelForm):
    class Meta:
        model = CreditRating
        fields = [
            'user',
            'sector',
            'liquidity_ratio',
            'leverage_ratio',
            'profitability_ratio',
            'debt_service_coverage_ratio',
            'financial_stmt_quality',
            'maker',
            'checker',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # widgets, labels, or other customizations I should add here later
