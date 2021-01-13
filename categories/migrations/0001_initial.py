# Generated by Django 2.2.5 on 2021-01-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=15)),
                ('kind', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
