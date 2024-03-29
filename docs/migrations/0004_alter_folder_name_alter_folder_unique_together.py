# Generated by Django 5.0.1 on 2024-02-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_alter_folder_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together={('name', 'parent')},
        ),
    ]
