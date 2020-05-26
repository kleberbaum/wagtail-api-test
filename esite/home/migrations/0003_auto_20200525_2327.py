# Generated by Django 2.2.9 on 2020-05-25 22:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200525_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='article',
        ),
        migrations.AddField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_about', wagtail.core.blocks.StructBlock([('pages', wagtail.core.blocks.StreamBlock([('page', wagtail.core.blocks.StructBlock([('boxes', wagtail.core.blocks.StreamBlock([('box', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, classname='full title', icon='title', null=True)), ('content', wagtail.core.blocks.RichTextBlock(blank=True, classname='full', null=True))], blank=False, null=True))], blank=False, null=True))], blank=False, null=True))], blank=False, null=True))], blank=False, icon='title', null=True))], null=True),
        ),
    ]
