# Generated by Django 4.2.1 on 2023-05-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_alter_posts_pro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='pro',
        ),
    ]
