# Generated by Django 2.2.5 on 2021-01-12 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='')),
                ('rating', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
