# Generated by Django 3.2.5 on 2021-11-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_question_ques_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ques_image',
            field=models.ImageField(blank=True, default='defaultt.png', null=True, upload_to='images/'),
        ),
    ]