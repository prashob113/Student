# Generated by Django 4.2 on 2023-04-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_chemistry_marks_alter_student_cs_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='physics_marks',
            field=models.PositiveIntegerField(max_length=2),
        ),
    ]
