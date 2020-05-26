# Generated by Django 2.2.9 on 2020-05-26 00:03

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200526_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_about', wagtail.core.blocks.StructBlock([('pages', wagtail.core.blocks.StreamBlock([('page', wagtail.core.blocks.StructBlock([('blink', wagtail.core.blocks.CharBlock(blank=True, classname='full')), ('use_image', wagtail.core.blocks.BooleanBlock(classname='full', default=False, help_text='Use picture instead of blink', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(classname='full', required=False)), ('boxes', wagtail.core.blocks.StreamBlock([('box', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, classname='full title', icon='title', null=True)), ('content', wagtail.core.blocks.RichTextBlock(blank=True, classname='full', null=True))], blank=False, icon='doc-full', null=True))], blank=False, null=True))], blank=False, icon='cogs', null=True))], blank=False, null=True))], blank=False, icon='radio-empty', null=True)), ('s_amodt', wagtail.core.blocks.StructBlock([('modt', wagtail.core.blocks.CharBlock(classname='full', default="Sky's The Limit", max_length=16))], blank=False, icon='pilcrow', null=True)), ('s_asharingan', wagtail.core.blocks.StructBlock([('sharingans', wagtail.core.blocks.StreamBlock([('sharingan', wagtail.core.blocks.StructBlock([('show_projects', wagtail.core.blocks.BooleanBlock(classname='full', default=True, help_text='Whether sh1, sh2, sh3 will be shown on this block', required=False)), ('sharingan_1', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True)), ('sharingan_2', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True)), ('sharingan_3', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True))], blank=False, null=True))])), ('teams', wagtail.core.blocks.StreamBlock([('team', wagtail.core.blocks.StructBlock([('show_team', wagtail.core.blocks.BooleanBlock(classname='full', default=False, help_text='Whether the team will be shown on this block', required=False)), ('nyan_title', wagtail.core.blocks.CharBlock(classname='full', default='The Team', max_length=16)), ('members', wagtail.core.blocks.StreamBlock([('member', wagtail.core.blocks.StructBlock([('pic', wagtail.images.blocks.ImageChooserBlock(blank=True, classname='full')), ('name', wagtail.core.blocks.CharBlock(blank=True, classname='full', default='', max_length=16)), ('description', wagtail.core.blocks.CharBlock(classname='full', default='', max_length=128))], blank=False, icon='user', null=True))], blank=False))], blank=False, null=True))]))], blank=False, icon='view', null=True))], null=True),
        ),
    ]
