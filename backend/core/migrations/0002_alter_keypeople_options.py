# Generated by Django 4.2 on 2024-10-12 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keypeople',
            options={'ordering': ('key_people_name',), 'verbose_name': 'Key people сотрудника', 'verbose_name_plural': 'Key people сотрудников'},
        ),
    ]