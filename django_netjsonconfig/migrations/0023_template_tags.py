# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-14 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('django_netjsonconfig', '0022_update_model_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='django_netjsonconfig_taggedtemplate_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'abstract': False,
                'verbose_name': 'Tagged item',
            },
        ),
        migrations.CreateModel(
            name='TemplateTag',
            fields=[
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'abstract': False,
                'verbose_name': 'Tag',
            },
        ),
        migrations.AddField(
            model_name='taggedtemplate',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='django_netjsonconfig_taggedtemplate_items', to='django_netjsonconfig.TemplateTag'),
        ),
        migrations.AddField(
            model_name='template',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of template tags, may be used to ease auto configuration with specific settings (eg: 4G, mesh, WDS, VPN, ecc.)', through='django_netjsonconfig.TaggedTemplate', to='django_netjsonconfig.TemplateTag', verbose_name='Tags'),
        ),
    ]
