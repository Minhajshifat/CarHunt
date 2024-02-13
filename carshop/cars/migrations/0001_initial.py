# Generated by Django 5.0 on 2024-02-10 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carBrand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/media/uploads/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carBrand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('body', models.TextField(max_length=200)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cars.carmodel')),
            ],
        ),
    ]
