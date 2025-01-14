# Generated by Django 5.1.4 on 2025-01-09 16:41

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "wagtail_localize_test",
            "0003_alter_header_locale_alter_navigationlink_locale_and_more",
        ),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "media",
                    wagtail.fields.StreamField(
                        [("audio", 0)],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtailmedia.blocks.AudioChooserBlock",
                                (),
                                {"icon": "media", "label": "Audio"},
                            )
                        },
                        help_text="Audio Dateien verlinken",
                        verbose_name="Medien",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
