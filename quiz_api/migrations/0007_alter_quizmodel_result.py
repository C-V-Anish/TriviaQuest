# Generated by Django 4.2.1 on 2023-05-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0006_choice_quizmodel_delete_quiz_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='result',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
