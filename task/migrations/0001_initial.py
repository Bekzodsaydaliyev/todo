# Generated by Django 4.1.5 on 2023-01-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=222)),
                ('content', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now=True, null=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
