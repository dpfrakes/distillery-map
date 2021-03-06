# Generated by Django 3.0.5 on 2020-05-09 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirginiaPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200, unique=True)),
                ('unique_id', models.CharField(help_text='Unique to product but not size/price', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('size', models.CharField(max_length=20)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('product_uri', models.URLField(blank=True, null=True)),
                ('hierarchy_division', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_class', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_category', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_type', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_detail', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_fact', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_imported', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_flavored', models.CharField(blank=True, max_length=50, null=True)),
                ('hierarchy_vap', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('scotch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entities.Scotch')),
            ],
            options={
                'verbose_name': 'Virginia price info',
                'verbose_name_plural': 'Virginia',
            },
        ),
    ]
