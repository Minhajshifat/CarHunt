# Generated by Django 5.0 on 2024-02-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/media/uploads/'),
        ),
    ]