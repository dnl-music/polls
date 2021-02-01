# Generated by Django 2.2.10 on 2021-01-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default='Hello!', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='point',
            field=models.ManyToManyField(blank=True, to='polls_app.QuestionPoint'),
        ),
    ]
