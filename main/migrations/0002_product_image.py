# Generated by Django 4.2.6 on 2023-10-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_images/default_image.jpg', upload_to='product_images/'),
        ),
    ]
