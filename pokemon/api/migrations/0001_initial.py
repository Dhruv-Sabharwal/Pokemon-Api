# Generated by Django 2.2.7 on 2019-12-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedex_num', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('type_1', models.CharField(max_length=200)),
                ('type_2', models.CharField(max_length=200)),
                ('total', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('sp_attack', models.IntegerField(default=0)),
                ('sp_defense', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('generation', models.IntegerField(default=0)),
                ('legendary', models.CharField(max_length=200)),
            ],
        ),
    ]
