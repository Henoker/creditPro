from django.contrib import admin
from .models import (FinancialRiskParameter, QualityOfFinancialStatements, LoanType, Loan, 
                    CreditAnalyst, CreditDecision , BusinessRiskParameter, MarketRiskParameter, 
                    ManagementExperienceRiskParameter, ManagemementSuccessionRiskParameter, 
                    ManagementQualificationRiskParameter, LengthOfBorrowingRelationshipRiskParameter, 
                    IntegrityOfCustomerRiskParameter, OverdraftSwingHighestDebtRiskParameter, 
                    OverdraftSwingLowestDebtRiskParameter, OverdraftTurnoverRiskParameter, 
                    TermLoanCurrentRiskParameter, TermLoanSettledRiskParameter, 
                    LcFacilitySettlementRiskParameter, LcFacilityTurnoverRiskParameter,
                    MerchandiseLoanTurnoverRiskParameter, MerchandiseSettlementRiskParameter,
                    PSEForCoffeeSeasameTurnoverRiskParameter, PSEForLeathermfgTurnoverRiskParameter,
                    PSEForOtherTradingTurnoverRiskParameter, LetterOfGuaranteeSettlementRiskParameter
                )


class FinancialRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('sector', 'measurement', 'min_value', 'max_value', 'score')
    list_filter = ('sector', 'measurement')
    search_fields = ('sector', 'measurement')
    ordering = ('sector', 'measurement')
    list_per_page = 20  

admin.site.register(FinancialRiskParameter, FinancialRiskParameterAdmin)

class QualityOfFinancialStatementsAdmin(admin.ModelAdmin):
    list_display = ('loan_exposure', 'score', 'description')
    list_filter = ('loan_exposure',)
    search_fields = ('loan_exposure',)
    ordering = ('loan_exposure',)
    list_per_page = 20  
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
    list_per_page = 20  

admin.site.register(MarketRiskParameter, MarketRiskAdmin)

class ManagementExperienceRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('management_experience', 'score', 'description')
    list_filter = ('management_experience',)
    search_fields = ('management_experience',)
    ordering = ('management_experience',)
    list_per_page = 20  

admin.site.register(ManagementExperienceRiskParameter, ManagementExperienceRiskParameterAdmin)

class ManagementQualificationRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('management_qualification', 'score', 'description')
    list_filter = ('management_qualification',)
    search_fields = ('management_qualification',)
    ordering = ('management_qualification',)
    list_per_page = 20

admin.site.register(ManagementQualificationRiskParameter, ManagementQualificationRiskParameterAdmin)

class ManagemementSuccessionRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('management_succession', 'score', 'description')
    list_filter = ('management_succession',)
    search_fields = ('management_succession',)
    ordering = ('management_succession',)
    list_per_page = 20  

admin.site.register(ManagemementSuccessionRiskParameter, ManagemementSuccessionRiskParameterAdmin)

class LengthOfBorrowingRelationshipRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('borrowing_length', 'score', 'description')
    list_filter = ('borrowing_length',)
    search_fields = ('borrowing_length',)
    ordering = ('borrowing_length',)
    list_per_page = 20  

admin.site.register(LengthOfBorrowingRelationshipRiskParameter, LengthOfBorrowingRelationshipRiskParameterAdmin)

class IntegrityOfCustomerRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('Integrity_risk', 'score', 'description')
    list_filter = ('Integrity_risk',)
    search_fields = ('Integrity_risk',)
    ordering = ('Integrity_risk',)
    list_per_page = 20  

admin.site.register(IntegrityOfCustomerRiskParameter, IntegrityOfCustomerRiskParameterAdmin)

class OverdraftSwingHighestDebtRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('highest_debt', 'score', 'description')
    list_filter = ('highest_debt',)
    search_fields = ('highest_debt',)
    ordering = ('highest_debt',)
    list_per_page = 20  

admin.site.register(OverdraftSwingHighestDebtRiskParameter, OverdraftSwingHighestDebtRiskParameterAdmin)

class OverdraftSwingLowestDebtRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('lowest_debt', 'score', 'description')
    list_filter = ('lowest_debt',)
    search_fields = ('lowest_debt',)
    ordering = ('lowest_debt',)
    list_per_page = 20  

admin.site.register(OverdraftSwingLowestDebtRiskParameter, OverdraftSwingLowestDebtRiskParameterAdmin)

class OverdraftTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('overdraft_turnover', 'score', 'description')
    list_filter = ('overdraft_turnover',)
    search_fields = ('overdraft_turnover',)
    ordering = ('overdraft_turnover',)
    list_per_page = 20  

admin.site.register(OverdraftTurnoverRiskParameter, OverdraftTurnoverRiskParameterAdmin)

class TermLoanCurrentRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('current_loan', 'score', 'description')
    list_filter = ('current_loan',)
    search_fields = ('current_loan',)
    ordering = ('current_loan',)
    list_per_page = 20  

admin.site.register(TermLoanCurrentRiskParameter, TermLoanCurrentRiskParameterAdmin)

class TermLoanSettledRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('settled_loan', 'score', 'description')
    list_filter = ('settled_loan',)
    search_fields = ('settled_loan',)
    ordering = ('settled_loan',)
    list_per_page = 20  

admin.site.register(TermLoanSettledRiskParameter, TermLoanSettledRiskParameterAdmin)

class LcFacilitySettlementRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('settled_lc', 'score', 'description')
    list_filter = ('settled_lc',)
    search_fields = ('settled_lc',)
    ordering = ('settled_lc',)
    list_per_page = 20  

admin.site.register(LcFacilitySettlementRiskParameter, LcFacilitySettlementRiskParameterAdmin)

class LcFacilityTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('lc_turnover', 'score', 'description')
    list_filter = ('lc_turnover',)
    search_fields = ('lc_turnover',)
    ordering = ('lc_turnover',)
    list_per_page = 20  

admin.site.register(LcFacilityTurnoverRiskParameter, LcFacilityTurnoverRiskParameterAdmin)

class MerchandiseLoanTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('merchandise_turnover', 'score', 'description')
    list_filter = ('merchandise_turnover',)
    search_fields = ('merchandise_turnover',)
    ordering = ('merchandise_turnover',)
    list_per_page = 20  

admin.site.register(MerchandiseLoanTurnoverRiskParameter, MerchandiseLoanTurnoverRiskParameterAdmin)

class MerchandiseSettlementRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('settled_ml', 'score', 'description')
    list_filter = ('settled_ml',)
    search_fields = ('settled_ml',)
    ordering = ('settled_ml',)
    list_per_page = 20  

admin.site.register(MerchandiseSettlementRiskParameter, MerchandiseSettlementRiskParameterAdmin)


class PSEForCoffeeSeasameTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('pse_coffee_turnover', 'score', 'description')
    list_filter = ('pse_coffee_turnover',)
    search_fields = ('pse_coffee_turnover',)
    ordering = ('pse_coffee_turnover',)
    list_per_page = 20  

admin.site.register(PSEForCoffeeSeasameTurnoverRiskParameter, PSEForCoffeeSeasameTurnoverRiskParameterAdmin)

class PSEForLeathermfgTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('pse_leather_turnover', 'score', 'description')
    list_filter = ('pse_leather_turnover',)
    search_fields = ('pse_leather_turnover',)
    ordering = ('pse_leather_turnover',)
    list_per_page = 20  

admin.site.register(PSEForLeathermfgTurnoverRiskParameter, PSEForLeathermfgTurnoverRiskParameterAdmin)

class PSEForOtherTradingTurnoverRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('pse_other_turnover', 'score', 'description')
    list_filter = ('pse_other_turnover',)
    search_fields = ('pse_other_turnover',)
    ordering = ('pse_other_turnover',)
    list_per_page = 20  

admin.site.register(PSEForOtherTradingTurnoverRiskParameter, PSEForOtherTradingTurnoverRiskParameterAdmin)

class LetterOfGuaranteeSettlementRiskParameterAdmin(admin.ModelAdmin):
    list_display = ('lg_settlement', 'score', 'description')
    list_filter = ('lg_settlement',)
    search_fields = ('lg_settlement',)
    ordering = ('lg_settlement',)
    list_per_page = 20  

admin.site.register(LetterOfGuaranteeSettlementRiskParameter, LetterOfGuaranteeSettlementRiskParameterAdmin)