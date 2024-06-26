# Generated by Django 4.2.2 on 2024-06-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_products_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="products",
            options={
                "permissions": [
                    ("set_published_status", "Can publish product"),
                    ("change_description", "Can change product description"),
                    ("change_category", "Can change product category"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="products",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Признак публикации"),
        ),
    ]
