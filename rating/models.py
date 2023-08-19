from django.db import models
from django.conf import settings

from accounts.models import CustomUser



# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Add other fields related to the sector if needed

    def __str__(self):
        return self.name
class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.branch_name
class Borrower(models.Model):
    CLASS = [
        ("Retail", "retail"),
        ("Business", "Business"),
        ("Corporate", "Corporate"),
    ]
    borrower_name = models.CharField(max_length=50)
    borrower_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    borrower_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    borrower_class = models.Case(choices=CLASS, default='', max_length=100)
    LAF_NO = models.CharField(max_length=100)
    Loan_code= models.CharField(max_length=100)

    def total_loan_exposure(self):
        """
        Calculate the total loan exposure for this customer by summing up all loan facilities.
        """
        loan_facilities = self.loanfacility_set.all()
        total_exposure = sum([facility.exposure_amount for facility in loan_facilities])
        return total_exposure

    def __str__(self):
        return self.borrower_name

class LiquidityRating(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.PositiveIntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.PositiveIntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.PositiveIntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.PositiveIntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sector} - Liquidity Rating"

class LeverageRating(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.PositiveIntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.PositiveIntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.PositiveIntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.PositiveIntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sector} - Leverage Rating"
class ProfitabilityRating(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.PositiveIntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.PositiveIntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.PositiveIntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.PositiveIntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sector} - Profitability Rating"
    
class Debt_service_coverage_ratio(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.PositiveIntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.PositiveIntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.PositiveIntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.PositiveIntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sector} - debt_service_coverage_ratio"
class LoanFacility(models.Model):
    LOAN_FACILITY_CHOICES = (
        ('Overdraft', 'Overdraft Facility'),
        ('TermLoan', 'Term Loan'),
        ('LetterOfCredit', 'Letter of Credit Facility'),
        ('MerchandiseLoan', 'Merchandise Loan'),
        ('PreShipmentExportCredit', 'Pre-shipment Export Credit Facility'),
        ('RevolvingExportCredit', 'Revolving Export Credit'),
        ('LetterOfGuarantee', 'Letter of Guarantee'),
    )

    customer = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    facility_type = models.CharField(max_length=50, choices=LOAN_FACILITY_CHOICES)
    exposure_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_facility_type_display()} - {self.exposure_amount}" 
    
class Financial_stmt_quality_Rating(models.Model):
    AUDIT_TYPE_CHOICES = (
        ('Audited', 'Audited Financial Statement'),
        ('Provisional', 'Provisional Financial Statement'),
        ('CommercialReport', 'Commercial Credit Report'),
    )

    AUDIT_DISCREPANCY_CHOICES = (
        ('None', 'No Discrepancy'),
        ('Major', 'Major Discrepancy'),
        ('Minor', 'Minor Discrepancy'),
    )

    customer = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    audit_type = models.CharField(max_length=50, choices=AUDIT_TYPE_CHOICES)
    audit_discrepancy = models.CharField(max_length=50, choices=AUDIT_DISCREPANCY_CHOICES)

    def calculate_score(self):
        score = 0
        
        if self.customer.loan_exposure > 1000000:
            if self.audit_type == 'Audited':
                score = 6
            elif self.audit_type == 'Provisional':
                score = 5
            elif self.audit_type == 'CommercialReport':
                score = 0
        else:
            if self.audit_type == 'Audited':
                score = 6
            elif self.audit_type == 'Provisional':
                score = 5
            elif self.audit_type == 'CommercialReport':
                score = 3
        
        if self.audit_discrepancy == 'Major':
            score -= 5
        elif self.audit_discrepancy == 'Minor':
            score -= 2
        
        return max(0, score)  # Ensure the score is not negative

    def __str__(self):
        return f"Score: {self.calculate_score()} for {self.customer.borrower_name}"

class CreditRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    maker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='maker_ratings', on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.MAKER})
    checker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='checker_ratings', on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.CHECKER}, null=True, blank=True)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_ratings', on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.STAFF}, null=True, blank=True)
    
    def calculate_rating_score(self, rating_model, parameter_value):
        """
        Calculate the rating score based on the parameter value and sector-specific rules.
        """
        rating = rating_model.objects.filter(sector=self.sector).first()

        if rating:
            if rating.range_1_lower_bound <= parameter_value <= rating.range_1_upper_bound:
                return rating.range_1_score
            elif rating.range_2_lower_bound <= parameter_value <= rating.range_2_upper_bound:
                return rating.range_2_score
            elif rating.range_3_lower_bound <= parameter_value <= rating.range_3_upper_bound:
                return rating.range_3_score
            elif rating.range_4_lower_bound <= parameter_value <= rating.range_4_upper_bound:
                return rating.range_4_score
            elif rating.range_5_lower_bound <= parameter_value <= rating.range_5_upper_bound:
                return rating.range_5_score
            else:
                return 0
        else:
            return 0
    
    def calculate_total_financial_risk(self):
        liquidity_score = self.calculate_rating_score(LiquidityRating, self.liquidity_ratio)
        leverage_score = self.calculate_rating_score(LeverageRating, self.leverage_ratio)
        profitability_score = self.calculate_rating_score(ProfitabilityRating, self.profitability_ratio)
        dscr_score = self.calculate_rating_score(Debt_service_coverage_ratio, self.debt_service_coverage_ratio)
        stmt_quality_score = Financial_stmt_quality_Rating.calculate_score()

        return liquidity_score + leverage_score + profitability_score + dscr_score + stmt_quality_score

    def save(self, *args, **kwargs):
        self.financial_risk = self.calculate_total_financial_risk()
        super().save(*args, **kwargs)
