# Generated by Django 2.0.4 on 2018-06-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_comments_comments_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_text', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]