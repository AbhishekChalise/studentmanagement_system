# Generated by Django 5.1.3 on 2024-11-27 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(choices=[('ComputerScience', 'ComputerScience'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
