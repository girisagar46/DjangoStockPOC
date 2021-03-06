# Generated by Django 3.1.7 on 2021-03-15 23:28

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('symbol', models.CharField(max_length=5, unique=True, verbose_name='NASDAQ Ticker Symbol')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Date when the stock data was recorded.')),
                ('open', models.FloatField(help_text='Opening price of the stock that day.')),
                ('high', models.FloatField(help_text='High price of the stock on that day.')),
                ('low', models.FloatField(help_text='Low price of the stock on that day.')),
                ('close', models.FloatField(help_text='Closing price of stock that day.')),
                ('adj_close', models.FloatField(help_text='Adjusted closing price of stock that day.')),
                ('volume', models.FloatField(help_text='Number of shares traded in a stock')),
                ('unadjusted_volume', models.FloatField(verbose_name='Unadjusted volume that day.')),
                ('change', models.FloatField(verbose_name='Price difference that occurs between two points in time.')),
                ('change_percent', models.FloatField(verbose_name='Change percentage in price.')),
                ('vwap', models.FloatField(help_text='Volume Weighted Average Price')),
                ('label', models.CharField(help_text='Label of the stock. Generally the date representation.', max_length=30)),
                ('change_over_time', models.FloatField(help_text='Stock price change over time.')),
                ('company_symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.company')),
            ],
            options={
                'db_table': 'stock_history',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
