# Generated by Django 3.2.5 on 2023-11-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=255)),
                ('subcounty', models.CharField(max_length=255)),
                ('ward', models.CharField(max_length=255)),
                ('floor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.business')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.location')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.category'),
        ),
    ]
