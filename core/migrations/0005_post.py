# Generated by Django 5.1.5 on 2025-02-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post_type', models.CharField(choices=[('news', 'News'), ('event', 'Event'), ('announcement', 'Announcement')], default='news', max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
