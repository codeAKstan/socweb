# Generated by Django 5.1.3 on 2024-11-13 10:57

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('DF', 'DRAFT'), ('PB', 'PUBLISHED')], default='DF', max_length=12)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]