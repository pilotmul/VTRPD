# Generated by Django 5.1.4 on 2024-12-13 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spam', '0004_alter_click_options_alter_codesubmission_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='click',
            options={'verbose_name': 'Hvor mange har klikket', 'verbose_name_plural': 'Hvor mange har klikket'},
        ),
        migrations.AlterModelOptions(
            name='codesubmission',
            options={'verbose_name': 'Hvor mange har skrevet sin kode', 'verbose_name_plural': 'Hvor mange har skrevet sin kode'},
        ),
    ]
