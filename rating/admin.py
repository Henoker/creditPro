from django.contrib import admin
from .models import Borrower, Sector, Branch, LiquidityRating, LeverageRating, ProfitabilityRating, Debt_service_coverage_ratio,Financial_stmt_quality_Rating, CreditRating
# Register your models here.
admin.site.register(Borrower)
admin.site.register(Sector)
admin.site.register(Branch)
admin.site.register(LiquidityRating)
admin.site.register(LeverageRating)
admin.site.register(ProfitabilityRating)
admin.site.register(Debt_service_coverage_ratio)
admin.site.register(Financial_stmt_quality_Rating)
admin.site.register(CreditRating)


