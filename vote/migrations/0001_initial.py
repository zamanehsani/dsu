# Generated by Django 4.0.4 on 2022-05-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('code', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
