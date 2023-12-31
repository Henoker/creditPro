# Generated by Django 4.0.10 on 2023-08-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0006_overdraftswinghighestdebtriskparameter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermLoanCurrentRiskParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_loan', models.CharField(choices=[('regular repayments', 'regular repayments'), ('5-30 days in arrears', '5-30 days in arrears'), ('31-60 days in arrears', '31-60 days in arrears'), ('more than 60 days in arrears', 'more than 60 days in arrears')], max_length=100)),
                ('score', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TermLoanSettledRiskParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settled_loan', models.CharField(choices=[('settled with regular repayments', 'settled with regular repayments'), ('settled timely but with an elemwnt of irregularity', 'settled timely but with an elemwnt of irregularity'), ('settled within thirty days after due date', 'settled within thirty days after due date'), ('settled between 30 to 89 days after due date', 'settled between 30 to 89 days after due date'), ('settled after NPL or legal action', 'settled after NPL or legal action')], max_length=100)),
                ('score', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
