# Generated by Django 5.1.7 on 2025-04-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_title_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
