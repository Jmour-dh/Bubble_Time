# Generated by Django 5.0.4 on 2024-04-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_taste', models.CharField(max_length=50, null=True)),
                ('toppings', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'bubbles',
            },
        ),
    ]