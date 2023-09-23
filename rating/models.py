
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
    
class ManagementExperienceRiskParameter(models.Model):
       
    MANAGEMENT_EXPERIENCE_CHOICES = [
        ('if 51% and above of top management have more than 10 years experience', 'if 51% and above of top management have more than 10 years experience'),
        ('if 51% and above of top management have more than 7 years experience', 'if 51% and above of top management have more than 7 years experience'),
        ('if 51% and above of top management have more than 3 years experience', 'if 51% and above of top management have more than 3 years experience'),
        ('if 51% and above of top management have less than 3 years experience', 'if 51% and above of top management have less than 3 years experience')
    ]
    
    management_experience = models.CharField(max_length=100, choices=MANAGEMENT_EXPERIENCE_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.management_experience} - Management experience"

class ManagementQualificationRiskParameter(models.Model):
       
    MANAGEMENT_QUALIFICATION_CHOICES = [
        ('if 51% and above of top management are degree holders and above', 'if 51% and above of top management are degree holders and above'),
        ('if 51% and above of top management are diploma, degree and above holders', 'if 51% and above of top management are diploma, degree and above holders'),
        ('if 51% and above of top management are High School, diploma, degree and above holders', 'if 51% and above of top management are High School, diploma, degree and above holders'),
        ('if 51% and above of top management are below high school graduate', 'if 51% and above of top management are below high school graduate')
    ]
    
    management_qualification = models.CharField(max_length=100, choices=MANAGEMENT_QUALIFICATION_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.management_qualification} - Management qualification"

class ManagemementSuccessionRiskParameter(models.Model):
       
    MANAGEMENT_SUCCESSION_CHOICES = [
        ('ready succession', 'ready succession'),
        ('succession in question', 'succession in question')
    ]
    
    management_succession = models.CharField(max_length=100, choices=MANAGEMENT_SUCCESSION_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.management_succession} - Management succession"

class LengthOfBorrowingRelationshipRiskParameter(models.Model):
       
    BORROWING_LENGTH_CHOICES = [
        ('greater than 10 years', 'greater than 10 years'),
        ('5-9 years', '5-9 years'),
        ('2-4 years', '2-4 years'),
        ('1-2 years', '1-2 years'),
        ('less than 1 year', 'less than 1 year')
    ]
    
    borrowing_length = models.CharField(max_length=100, choices=BORROWING_LENGTH_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.borrowing_length} - Length of Borrwing Relationship" 
    
class IntegrityOfCustomerRiskParameter(models.Model):
       
    INTEGRITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    
    Integrity_risk = models.CharField(max_length=100, choices=INTEGRITY_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.Integrity_risk} - Integrity, Honesty and Coperation with the Bank" 
    
class OverdraftSwingHighestDebtRiskParameter(models.Model):
       
    HIGHEST_DEBT_CHOICES = [
        ('greater than 85%', 'greater than 85%'),
        ('60-84.9%', '60-84.9%'),
        ('less than 60%', 'less than 60%')
    ]
    
    highest_debt = models.CharField(max_length=100, choices=HIGHEST_DEBT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.highest_debt} - Overdraft Swing Highest Debt"
    
class OverdraftSwingLowestDebtRiskParameter(models.Model):
       
    LOWEST_DEBT_CHOICES = [
        ('at least credit balance within three month', 'at least credit balance within three month'),
        ('at least credit balance within six month', 'at least credit balance within six month'),
        ('at least 4% debt balance with a year', 'at least 4% debt balance with a year')
    ]
    
    lowest_debt = models.CharField(max_length=100, choices=LOWEST_DEBT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.lowest_debt} - Overdraft Swing Lowest Debt"
    
class OverdraftTurnoverRiskParameter(models.Model):
       
    TURNOVER_CHOICES = [
        ('greater than 3 times', 'greater than 3 times'),
        ('2-3 times', '2-3 times'),
        ('1-1.99 times', '1-1.99 times'),
        ('less than 1 times', 'less than 1 times')
    ]
    
    overdraft_turnover = models.CharField(max_length=100, choices=TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.overdraft_turnover} - Overdraft Turnover"
    
class TermLoanCurrentRiskParameter(models.Model):
       
    TERM_LOAN_CURRENT_CHOICES = [
        ('regular repayments', 'regular repayments'),
        ('5-30 days in arrears', '5-30 days in arrears'),
        ('31-60 days in arrears', '31-60 days in arrears'),
        ('more than 60 days in arrears', 'more than 60 days in arrears')
    ]
    
    current_loan = models.CharField(max_length=100, choices=TERM_LOAN_CURRENT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.current_loan} - Current Loan Term Loan Performance"   
    

class TermLoanSettledRiskParameter(models.Model):
       
    TERM_LOAN_SETTLED_CHOICES = [
        ('settled with regular repayments', 'settled with regular repayments'),
        ('settled timely but with an elemwnt of irregularity', 'settled timely but with an elemwnt of irregularity'),
        ('settled within thirty days after due date', 'settled within thirty days after due date'),
        ('settled between 30 to 89 days after due date', 'settled between 30 to 89 days after due date'),
        ('settled after NPL or legal action', 'settled after NPL or legal action')
    ]
    
    settled_loan = models.CharField(max_length=100, choices=TERM_LOAN_SETTLED_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.settled_loan} - Settled Loan Term Loan Performance"  

class LcFacilitySettlementRiskParameter(models.Model):
       
    LC_FACILITY_SETTLEMENT_CHOICES = [
        ('settled within  a week', 'settled within  a week'),
        ('settled within  three weeks', 'settled within  three weeks'),
        ('settled within a month', 'settled within a month'),
        ('settled after a month', 'settled after a month')
    ]
    
    settled_lc = models.CharField(max_length=100, choices=LC_FACILITY_SETTLEMENT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.settled_lc} - Settled LC Facility Loan Performance"   

class LcFacilityTurnoverRiskParameter(models.Model):
       
    LC_FACILITY_TURNOVER_CHOICES = [
        ('greater than 3 times', 'greater than 3 times'),
        ('2-3 times', '2-3 times'),
        ('1-1.99 times', '1-1.99 times'),
        ('less than 1 times', 'less than 1 times')
    ]
    
    lc_turnover = models.CharField(max_length=100, choices=LC_FACILITY_TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.lc_turnover} - LC Facility Turnover Loan Performance"      

class MerchandiseLoanTurnoverRiskParameter(models.Model):
       
    MERCHANDISE_TURNOVER_CHOICES = [
        ('greater than 2 times', 'greater than 2 times'),
        ('1.25-1.99 times', '1.25-1.99 times'),
        ('0.5-1.24 times', '0.5-1.24 times'),
        ('less than 0.5 times', 'less than 0.5 times')
    ]
    
    merchandise_turnover = models.CharField(max_length=100, choices=MERCHANDISE_TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.merchandise_turnover} - Merchandise Loan Turnover Performance"   

class MerchandiseSettlementRiskParameter(models.Model):
       
    MERCHANDISE_LOAN_SETTLEMENT_CHOICES = [
        ('settled all advances within 90 days', 'settled all advances within 90 days'),
        ('settled all advances within 120 days', 'settled all advances within 120 days'),
        ('settled within 145 days', 'settled within 145 days'),
        ('settled after 145 days', 'settled after 145 days')
    ]
    
    settled_ml = models.CharField(max_length=100, choices=MERCHANDISE_LOAN_SETTLEMENT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.settled_ml} - Settled Merchandise Loan Performance"   
    

     
class PSEForCoffeeSeasameTurnoverRiskParameter(models.Model):
       
    PSECOFFEE_TURNOVER_CHOICES = [
        ('greater than 2.5 times', 'greater than 2.5 times'),
        ('2-2.5 times', '2-2.5 times'),
        ('1.5-2 times', '1.5-2 times'),
        ('1-1.5 times', '1-1.5 times'),
        ('0.75-1 times', '0.75-1 times'),
        ('less than 0.75 times', 'less than 0.75 times')
    ]
    
    pse_coffee_turnover = models.CharField(max_length=100, choices=PSECOFFEE_TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.pse_coffee_turnover} - Preshipment Export facility for coffee and Seasame turnover"
    
class PSEForLeathermfgTurnoverRiskParameter(models.Model):
       
    PSELEATHER_TURNOVER_CHOICES = [
        ('greater than 2 times', 'greater than 2 times'),
        ('1.5-2 times', '1.5-2 times'),
        ('1.25-1.5 times', '1.25-1.5 times'),
        ('1-1.25 times', '1-1.25 times'),
        ('0.5-1 times', '0.5-1 times'),
        ('less than 0.5 times', 'less than 0.5 times')
    ]
    
    pse_leather_turnover = models.CharField(max_length=100, choices=PSELEATHER_TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.pse_leather_turnover} - Preshipment Export facility for leather and manufacturing turnover"  

class PSEForOtherTradingTurnoverRiskParameter(models.Model):
       
    PSEOTHER_TURNOVER_CHOICES = [
        ('greater than 2.75 times', 'greater than 2.75 times'),
        ('2-2.75 times', '2.2.75 times'),
        ('1.5-2 times', '1.5-2 times'),
        ('1-1.5 times', '1-1.5 times'),
        ('0.75-1 times', '0.75-1 times'),
        ('less than 0.75 times', 'less than 0.75 times')
    ]
    
    pse_other_turnover = models.CharField(max_length=100, choices=PSEOTHER_TURNOVER_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.pse_other_turnover} - Preshipment Export facility for other trading turnover"  

class LetterOfGuaranteeSettlementRiskParameter(models.Model):
       
    LG_SETTLEMENT_CHOICES = [
        ('settled/expired without claim', 'settled/expired without claim'),
        ('settled/expired after claim', 'settled/expired after claim')

    ]
    
    lg_settlement = models.CharField(max_length=100, choices=LG_SETTLEMENT_CHOICES)
    score = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.lg_settlement} - Letter of Guarantee facility Settlement Performance"     
 
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