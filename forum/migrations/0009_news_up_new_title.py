# Generated by Django 2.0.4 on 2018-06-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_bany_photo_raz_photo_rooms_photo_sport_zal_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_up',
            name='new_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
