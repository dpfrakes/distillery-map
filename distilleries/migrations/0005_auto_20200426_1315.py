# Generated by Django 3.0.5 on 2020-04-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distilleries', '0004_distillery_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distillery',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='distillery',
            name='logo_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
