# Generated by Django 5.1.4 on 2024-12-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_group_id_alter_groupcontributor_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='groupcontributor',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='initiatorgroupcontributor',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
