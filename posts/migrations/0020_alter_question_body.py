# Generated by Django 3.2.5 on 2021-11-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_question_ques_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.CharField(max_length=2559),
        ),
    ]
