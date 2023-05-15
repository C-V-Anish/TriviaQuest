# Generated by Django 4.2.1 on 2023-05-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0003_rename_options_quizmodel_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('choices', models.JSONField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]