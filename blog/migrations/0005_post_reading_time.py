# Generated by Django 4.1.3 on 2023-02-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="reading_time",
            field=models.IntegerField(default=1),
        ),
    ]
