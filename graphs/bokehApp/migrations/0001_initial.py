# Generated by Django 4.0.3 on 2022-04-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitalizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HospiWeeks', models.IntegerField()),
                ('HospiPati', models.IntegerField()),
            ],
        ),
    ]
