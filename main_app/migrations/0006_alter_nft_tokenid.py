# Generated by Django 4.2.3 on 2023-07-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_nft_tokenid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nft",
            name="tokenId",
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
