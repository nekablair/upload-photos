# Generated by Django 5.0.4 on 2024-04-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='django_uploads/files/covers'),
        ),
    ]
