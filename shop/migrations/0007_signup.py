# Generated by Django 3.0.8 on 2020-07-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('username', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=100)),
                ('pass1', models.CharField(max_length=100)),
                ('pass2', models.CharField(max_length=100)),
            ],
        ),
    ]
