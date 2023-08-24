from django.contrib import admin
from .models import FinancialRiskParameter, QualityOfFinancialStatements

class FinancialRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('sector', 'measurement', 'min_value', 'max_value', 'score')
    list_filter = ('sector', 'measurement')
    search_fields = ('sector', 'measurement')
    ordering = ('sector', 'measurement')
    list_per_page = 20  # Number of items to display per page

admin.site.register(FinancialRiskParameter, FinancialRiskParameterAdmin)

class QualityOfFinancialStatementsAdmin(admin.ModelAdmin):
    list_display = ('loan_exposure', 'score', 'description')
    list_filter = ('loan_exposure',)
    search_fields = ('loan_exposure',)
    ordering = ('loan_exposure',)
    list_per_page = 20  # Number of items to display per page

admin.site.register(QualityOfFinancialStatements, QualityOfFinancialStatementsAdmin)


