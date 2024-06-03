# Generated by Django 5.0.6 on 2024-06-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_from', models.CharField(max_length=3, verbose_name='Перевод с')),
                ('language_to', models.CharField(max_length=3, verbose_name='Перевод на')),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Перевод',
            },
        ),
    ]