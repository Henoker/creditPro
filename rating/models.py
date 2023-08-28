
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
        return f"{self.loan_exposure} - Quality of Financial Statement"

class BusinessRiskParameter(models.Model):
       
    INDUSTRY_OUTLOOK_CHOICES = [
        ('Favorable', 'Favorable'),
        ('Stable', 'stable'),
        ('unstable', 'unstable')
    ]
    
    industry_outlook = models.CharField(max_length=100, choices=INDUSTRY_OUTLOOK_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.industry_outlook} - Industy Outlook and Growth"

class MarketRiskParameter(models.Model):
       
    MARKET_SHARE_CHOICES = [
        ('Dominant', 'Dominant'),
        ('Average', 'Average'),
        ('weak', 'weak')
    ]
    
    market_share = models.CharField(max_length=100, choices=MARKET_SHARE_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.market_share} - Market Share"


class LoanType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create the Loans and Advances model
class Loan(models.Model):
    loan_id = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.PositiveIntegerField(help_text="Term in months")
    disbursement_date = models.DateField()
    maturity_date = models.DateField()
    collateral = models.TextField(blank=True, null=True)
    collateral_amount = models.DecimalField(max_digits=13, decimal_places=2)

    # Add any additional fields as needed

    def __str__(self):
        return f"Loan ID: {self.loan_id}, Type: {self.loan_type}"
    
class CreditAnalyst(models.Model):
    analyst_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=50)
    

    # Add any additional fields as needed

    def __str__(self):
        return f"Analyst ID: {self.analyst_id}, Name: {self.name}"

# Create the Credit Decisions model
class CreditDecision(models.Model):
    DECISION_CHOICES = (
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
        ('Pending', 'Pending'),
    )

    decision_id = models.CharField(max_length=20, unique=True)
    loan_id = models.CharField(max_length=20)
    analyst = models.ForeignKey(CreditAnalyst, on_delete=models.CASCADE)
    date_of_decision = models.DateField()
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES, default='Pending')
    comments = models.TextField(blank=True, null=True)

    # Add any additional fields as needed

    def __str__(self):
        return f"Decision ID: {self.decision_id}, Loan ID: {self.loan_id}, Analyst: {self.analyst.name}, Decision: {self.get_decision_display()}"