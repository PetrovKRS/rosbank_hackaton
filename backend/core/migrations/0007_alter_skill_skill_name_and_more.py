# Generated by Django 4.2 on 2024-10-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_employeeskill_actual_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название навыка'),
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('employee_id', 'email'), name='unique_first_name_email', violation_error_message='Сотрудник с таким именем и почтой уже существует.'),
        ),
        migrations.AddConstraint(
            model_name='employeecompetency',
            constraint=models.UniqueConstraint(fields=('employee', 'competency'), name='unique_employee_competency'),
        ),
        migrations.AddConstraint(
            model_name='employeedevelopmentplan',
            constraint=models.UniqueConstraint(fields=('employee', 'development_plan'), name='unique_employee_development_plan'),
        ),
        migrations.AddConstraint(
            model_name='employeegrade',
            constraint=models.UniqueConstraint(fields=('employee', 'grade'), name='unique_employee_grade'),
        ),
        migrations.AddConstraint(
            model_name='employeeposition',
            constraint=models.UniqueConstraint(fields=('employee', 'position'), name='unique_employee_position'),
        ),
        migrations.AddConstraint(
            model_name='employeeskill',
            constraint=models.UniqueConstraint(fields=('employee', 'skill'), name='unique_employee_skill'),
        ),
        migrations.AddConstraint(
            model_name='employeeteam',
            constraint=models.UniqueConstraint(fields=('employee', 'team'), name='unique_employee_team'),
        ),
        migrations.AddConstraint(
            model_name='employeetrainingapplication',
            constraint=models.UniqueConstraint(fields=('employee', 'training_application'), name='unique_employee_training_application'),
        ),
    ]