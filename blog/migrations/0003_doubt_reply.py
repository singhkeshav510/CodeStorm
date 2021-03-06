# Generated by Django 3.0.4 on 2020-05-20 05:59

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20200520_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('que_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doubt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Doubt')),
            ],
        ),
    ]
