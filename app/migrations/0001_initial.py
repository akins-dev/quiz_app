# Generated by Django 3.2.14 on 2022-10-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number_of_question', models.IntegerField(default=30)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
