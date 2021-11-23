# Generated by Django 3.2.9 on 2021-11-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='Anon', max_length=100)),
                ('author_email', models.EmailField(blank=True, default='', max_length=254)),
                ('text', models.TextField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_time'],
            },
        ),
    ]
