from django.db import models

# Create your models here.
class Sector(models.Model):
    SECTOR_CHOICES = [
        ('Agriculture', 'Agriculture'),
        ('Manufacturing', 'Manufacturing'),
        # Add more sector choices as needed
    ]
    sector_name = models.CharField(max_length=100, choices=SECTOR_CHOICES)
    # Add other fields related to the sector if needed

    def __str__(self):
        return self.sector_name

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.branch_name

class Borrower(models.Model):
    CLASS = [
        ("Retail", "Retail"),
        ("Business", "Business"),
        ("Corporate", "Corporate"),
    ]
    borrower_name = models.CharField(max_length=50)
    borrower_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    borrower_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    borrower_class = models.CharField(choices=CLASS, default='', max_length=100)
    LAF_NO = models.CharField(max_length=100)
    Loan_code = models.CharField(max_length=100)

    # def total_loan_exposure(self):
    #     """
    #     Calculate the total loan exposure for this customer by summing up all loan facilities.
    #     """
    #     loan_facilities = self.loanfacility_set.all()
    #     total_exposure = sum([facility.exposure_amount for facility in loan_facilities])
    #     return total_exposure

    def __str__(self):
        return self.borrower_name