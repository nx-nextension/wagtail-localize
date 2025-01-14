# Generated by Django 5.1.4 on 2025-01-14 16:09

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize_test", "0004_audiopage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiopage",
            name="media",
            field=wagtail.fields.StreamField(
                [("audio", 0), ("image", 1)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtailmedia.blocks.AudioChooserBlock",
                        (),
                        {"icon": "media", "label": "Audio"},
                    ),
                    1: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"icon": "media", "label": "Image"},
                    ),
                },
                help_text="Audio Dateien verlinken",
                verbose_name="Medien",
            ),
        ),
    ]
