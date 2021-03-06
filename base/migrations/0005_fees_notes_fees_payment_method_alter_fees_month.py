# Generated by Django 4.0 on 2022-02-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_fees_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='Notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fees',
            name='payment_method',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fees',
            name='month',
            field=models.CharField(choices=[('one_time', 'One Time'), ('january', 'January'), ('feburary', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'Novemeber'), ('december', 'December')], default='one_time', max_length=15),
        ),
    ]
