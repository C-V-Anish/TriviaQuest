# Generated by Django 4.2.1 on 2023-05-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0004_quiz_remove_quizmodel_choices_delete_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='choices',
            field=models.JSONField(null=True),
        ),
    ]
