# Generated by Django 3.2.14 on 2022-10-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_phy101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Phy101',
            new_name='Question',
        ),
    ]