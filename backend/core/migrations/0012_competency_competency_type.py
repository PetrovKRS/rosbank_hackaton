# Generated by Django 4.2 on 2024-10-10 13:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_skill_skill_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="competency",
            name="competency_type",
            field=models.CharField(
                choices=[("hard", "Hard"), ("soft", "Soft")],
                default=core.models.SkillTypeEnum["HARD"],
                max_length=4,
                verbose_name="Тип компетенции",
            ),
        ),
    ]