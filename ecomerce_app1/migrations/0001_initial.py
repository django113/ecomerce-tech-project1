# Generated by Django 4.1 on 2022-08-27 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='', upload_to='Products')),
                ('description', models.TextField()),
                ('colors', models.CharField(max_length=50)),
                ('grade', models.CharField(choices=[('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1')], max_length=50)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=50)),
                ('quality', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Big', 'Big'), ('Other', 'Other')], max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]