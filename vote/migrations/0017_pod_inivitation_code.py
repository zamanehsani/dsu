# Generated by Django 4.0.4 on 2022-05-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0016_alter_podmember_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pod',
            name='inivitation_code',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]