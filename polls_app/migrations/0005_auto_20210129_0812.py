# Generated by Django 2.2.10 on 2021-01-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0004_userquestion_question_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestion',
            name='question_point',
            field=models.ManyToManyField(blank=True, to='polls_app.QuestionPoint'),
        ),
    ]