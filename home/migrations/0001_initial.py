# Generated by Django 5.0.1 on 2024-02-04 06:12

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=1, max_digits=4)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET('USER_NOT_FOUND'), related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=models.SET('USER_NOT_FOUND'), related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET('USER_NOT_FOUND'), related_name='commented_by', to=settings.AUTH_USER_MODEL)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.document')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=1, max_digits=4)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=models.SET('USER_NOT_FOUND'), related_name='h_created_by', to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=models.SET('DOCUMENT_NOT_FOUND'), related_name='history', to='home.document')),
                ('updated_by', models.ForeignKey(on_delete=models.SET('USER_NOT_FOUND'), related_name='h_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
