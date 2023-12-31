# Generated by Django 3.2.21 on 2023-11-21 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0011_bankmodel_banktransactionhistory_banktransactionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False, verbose_name='BILLID')),
                ('billdate', models.DateField()),
                ('supplyplace', models.CharField(default='', max_length=100)),
                ('pay_method', models.CharField(default='', max_length=255, null=True)),
                ('cheque_no', models.CharField(default='', max_length=255, null=True)),
                ('upi_no', models.CharField(default='', max_length=255, null=True)),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('igst', models.CharField(default=0, max_length=100, null=True)),
                ('cgst', models.CharField(default=0, max_length=100, null=True)),
                ('sgst', models.CharField(default=0, max_length=100, null=True)),
                ('taxamount', models.CharField(default=0, max_length=100, null=True)),
                ('adjust', models.CharField(default=0, max_length=100, null=True)),
                ('grandtotal', models.FloatField(default=0, null=True)),
                ('advance', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.CharField(blank=True, max_length=255, null=True)),
                ('tot_bill_no', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=20)),
                ('transactiondate', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('purchasebill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.purchasebill')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('tax', models.CharField(max_length=100)),
                ('discount', models.CharField(default=0, max_length=100, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.itemmodel')),
                ('purchasebill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.purchasebill')),
            ],
        ),
    ]
