# Generated by Django 4.2.1 on 2023-05-14 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0005_alter_quiz_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('result', models.CharField(max_length=10)),
                ('choices', models.ManyToManyField(to='quiz_api.choice')),
            ],
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_api.quizmodel'),
        ),
    ]
