
from django.db import models
class FinancialRiskParameter(models.Model):
    SECTOR_CHOICES = [
        ('Agriculture', 'Agriculture'),
        ('Manufacturing', 'Manufacturing'),
        ('Leather', 'Leather'),
        ('Export', 'Export'),
        ('Construction', 'Construction'),
        ('DTS', 'DTS'),
        ('Import', 'Import'),
        ('Others', 'Others'), 
    ]
    
    MEASUREMENT_CHOICES = [
        ('Leverage Ratio', 'Leverage Ratio'),
        ('Liquidity Ratio', 'Liquidity Ratio'),
        ('Profitability Ratio', 'Profitability Ratio'),
        ('Debt Service Coverage Ratio', 'Debt Service Coverage Ratio'),
    ]
    
    sector = models.CharField(max_length=100, choices=SECTOR_CHOICES)
    measurement = models.CharField(max_length=100, choices=MEASUREMENT_CHOICES)
    min_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_value = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.sector} - {self.measurement}"

    class Meta:
        unique_together = ['sector', 'measurement', 'min_value', 'max_value']

class QualityOfFinancialStatements(models.Model):
       
    LOAN_EXPOSURE_CHOICES = [
        ('Greater than or equal to 1 million', 'Greater than or equal to 1 million'),
        ('Less than 1 million', 'Less than 1 million'),
    ]
    
    loan_exposure = models.CharField(max_length=100, choices=LOAN_EXPOSURE_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.loan_exposure} - Quality of Financial Statements"