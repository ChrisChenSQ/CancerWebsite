# Generated by Django 3.2.4 on 2021-07-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.TextField(max_length=50, verbose_name='Image_name')),
                ('image_path', models.TextField(verbose_name='Image_path')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Image',
            },
        ),
    ]
