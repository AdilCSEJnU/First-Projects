# Generated by Django 5.1.6 on 2025-02-25 18:23

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Bangla', 'Bangla'), ('English', 'English'), ('Hindi', 'Hindi'), ('Urdu', 'Urdu'), ('Arabic', 'Arabic')], default='Bangla', max_length=100),
        ),
    ]
