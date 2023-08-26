# Generated by Django 4.0.10 on 2023-08-26 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditAnalyst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analyst_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_information', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('experience_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('term', models.PositiveIntegerField(help_text='Term in months')),
                ('disbursement_date', models.DateField()),
                ('maturity_date', models.DateField()),
                ('collateral', models.TextField(blank=True, null=True)),
                ('collateral_amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('loan_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.loantype')),
            ],
        ),
        migrations.CreateModel(
            name='CreditDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision_id', models.CharField(max_length=20, unique=True)),
                ('loan_id', models.CharField(max_length=20)),
                ('date_of_decision', models.DateField()),
                ('decision', models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('comments', models.TextField(blank=True, null=True)),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.creditanalyst')),
            ],
        ),
    ]