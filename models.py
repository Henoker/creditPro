# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'accounts_customuser'


class AccountsCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AccountsCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CustomerBorrower(models.Model):
    id = models.BigAutoField(primary_key=True)
    borrower_name = models.CharField(max_length=50)
    borrower_class = models.CharField(max_length=100)
    laf_no = models.CharField(db_column='LAF_NO', max_length=100)  # Field name made lowercase.
    loan_code = models.CharField(db_column='Loan_code', max_length=100)  # Field name made lowercase.
    borrower_branch = models.ForeignKey('CustomerBranch', models.DO_NOTHING)
    borrower_sector = models.ForeignKey('CustomerSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer_borrower'


class CustomerBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer_branch'


class CustomerSector(models.Model):
    id = models.BigAutoField(primary_key=True)
    sector_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer_sector'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RatingBorrower(models.Model):
    id = models.BigAutoField(primary_key=True)
    borrower_name = models.CharField(max_length=50)
    laf_no = models.CharField(db_column='LAF_NO', max_length=100)  # Field name made lowercase.
    loan_code = models.CharField(db_column='Loan_code', max_length=100)  # Field name made lowercase.
    borrower_branch = models.ForeignKey('RatingBranch', models.DO_NOTHING)
    borrower_sector = models.ForeignKey('RatingSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_borrower'


class RatingBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rating_branch'


class RatingCreditrating(models.Model):
    id = models.BigAutoField(primary_key=True)
    checker = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING, blank=True, null=True)
    maker = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    staff = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_creditrating'


class RatingDebtServiceCoverageRatio(models.Model):
    id = models.BigAutoField(primary_key=True)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.IntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.IntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.IntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.IntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.IntegerField()
    sector = models.ForeignKey('RatingSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_debt_service_coverage_ratio'


class RatingFinancialStmtQualityRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    audit_type = models.CharField(max_length=50)
    audit_discrepancy = models.CharField(max_length=50)
    customer = models.ForeignKey(RatingBorrower, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_financial_stmt_quality_rating'


class RatingLeveragerating(models.Model):
    id = models.BigAutoField(primary_key=True)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.IntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.IntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.IntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.IntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.IntegerField()
    sector = models.ForeignKey('RatingSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_leveragerating'


class RatingLiquidityrating(models.Model):
    id = models.BigAutoField(primary_key=True)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.IntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.IntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.IntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.IntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.IntegerField()
    sector = models.ForeignKey('RatingSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_liquidityrating'


class RatingLoanfacility(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_type = models.CharField(max_length=50)
    exposure_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(RatingBorrower, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_loanfacility'


class RatingProfitabilityrating(models.Model):
    id = models.BigAutoField(primary_key=True)
    range_1_upper_bound = models.FloatField()
    range_1_lower_bound = models.FloatField()
    range_1_score = models.IntegerField()
    range_2_upper_bound = models.FloatField()
    range_2_lower_bound = models.FloatField()
    range_2_score = models.IntegerField()
    range_3_upper_bound = models.FloatField()
    range_3_lower_bound = models.FloatField()
    range_3_score = models.IntegerField()
    range_4_upper_bound = models.FloatField()
    range_4_lower_bound = models.FloatField()
    range_4_score = models.IntegerField()
    range_5_upper_bound = models.FloatField()
    range_5_lower_bound = models.FloatField()
    range_5_score = models.IntegerField()
    sector = models.ForeignKey('RatingSector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_profitabilityrating'


class RatingSector(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'rating_sector'
