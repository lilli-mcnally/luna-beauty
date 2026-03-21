import django.contrib.postgres.fields
from django.db import migrations, models

def convert_shades(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    for product in Product.objects.all():
        if product.shades and isinstance(product.shades, str):
            product.shades = [s.strip() for s in product.shades.split(',')]
            product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_shades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shades',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=200),
                blank=True,
                null=True,
                size=None
            ),
        ),
        migrations.RunPython(convert_shades),
    ]
