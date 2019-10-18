# Generated by Django 2.2.6 on 2019-10-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
