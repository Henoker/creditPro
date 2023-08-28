from django.contrib import admin
from .models import FinancialRiskParameter, QualityOfFinancialStatements, LoanType, Loan, CreditAnalyst, CreditDecision , BusinessRiskParameter, MarketRiskParameter


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

admin.site.register(LoanType)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'amount', 'loan_type')
    list_filter = ('loan_type',)
    search_fields = ('loan_type',)
    ordering = ('loan_type',)
    list_per_page = 20

admin.site.register(Loan, LoanAdmin)

class CreditAnalystAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

admin.site.register(CreditAnalyst, CreditAnalystAdmin)

class CreditDecisionAdmin(admin.ModelAdmin):
    list_display = ('decision_id', 'loan_id', 'analyst', 'date_of_decision', 'decision')
    list_filter = ('decision',)
    search_fields = ('decision',)
    ordering = ('decision',)
    list_per_page = 20
admin.site.register(CreditDecision, CreditDecisionAdmin)

class BusinessRiskAdmin(admin.ModelAdmin):
    list_display = ('industry_outlook', 'score', 'description')
    list_filter = ('industry_outlook',)
    search_fields = ('industry_outlook',)
    ordering = ('industry_outlook',)
    list_per_page = 20  # Number of items to display per page

admin.site.register(BusinessRiskParameter, BusinessRiskAdmin)

class MarketRiskAdmin(admin.ModelAdmin):
    list_display = ('market_share', 'score', 'description')
    list_filter = ('market_share',)
    search_fields = ('market_share',)
    ordering = ('market_share',)
    list_per_page = 20  # Number of items to display per page

admin.site.register(MarketRiskParameter, MarketRiskAdmin)