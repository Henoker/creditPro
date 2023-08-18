from django.db import models
from django.conf import settings

# Create your models here.
class CreditRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    maker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='maker_ratings', on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.MAKER})
    checker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='checker_ratings', on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.CHECKER}, null=True, blank=True)
    
    # Financial Risk Parameters
    liquidity_risk = models.PositiveIntegerField(default=0)
    profitability_risk = models.PositiveIntegerField(default=0)
    debt_service_coverage_ratio = models.PositiveIntegerField(default=0)
    leverage_risk = models.PositiveIntegerField(default=0)
    quality_of_financial_statements = models.PositiveIntegerField(default=0)

    @property
    def total_financial_risk(self):
        return (
            self.liquidity_risk + self.profitability_risk +
            self.debt_service_coverage_ratio + self.leverage_risk +
            self.quality_of_financial_statements
        )