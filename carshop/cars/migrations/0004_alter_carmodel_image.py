# Generated by Django 5.0 on 2024-02-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/'),
        ),
    ]