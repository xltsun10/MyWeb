# Generated by Django 4.2.7 on 2023-12-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='book', to='main.category'),
        ),
    ]
