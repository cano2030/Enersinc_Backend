# Generated by Django 4.0.6 on 2022-10-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_user_hobbie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hobbie',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo_doc',
            field=models.CharField(max_length=10),
        ),
    ]