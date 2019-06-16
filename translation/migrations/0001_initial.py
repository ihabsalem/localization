# Generated by Django 2.2 on 2019-06-16 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0001_initial'),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('language', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='language.Language')),
                ('source', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='source.Source')),
            ],
        ),
    ]
