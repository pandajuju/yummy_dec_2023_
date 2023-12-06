# Generated by Django 5.0 on 2023-12-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0002_alter_dishcategory_options_dish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('is_visible', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
