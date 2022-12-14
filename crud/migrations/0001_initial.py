# Generated by Django 4.0.6 on 2022-10-08 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_doc', models.CharField(max_length=100)),
                ('doc', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('hobbie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.hobbie')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
