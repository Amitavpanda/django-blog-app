# Generated by Django 3.2.6 on 2021-09-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog App', max_length=255),
        ),
    ]
