# Generated by Django 4.2.6 on 2023-10-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sathick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sal', models.IntegerField()),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ajith',
        ),
    ]
