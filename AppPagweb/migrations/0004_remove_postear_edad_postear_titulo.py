# Generated by Django 4.1.7 on 2023-03-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPagweb', '0003_remove_postear_publisher_postear_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postear',
            name='Edad',
        ),
        migrations.AddField(
            model_name='postear',
            name='Titulo',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
