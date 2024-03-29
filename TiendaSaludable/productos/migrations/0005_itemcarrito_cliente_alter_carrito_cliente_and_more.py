# Generated by Django 5.0 on 2024-01-10 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_remove_cliente_carrito_remove_itemcarrito_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrito',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='productos.cliente'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='productos.cliente'),
        ),
        migrations.AlterField(
            model_name='itemcarrito',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.carrito'),
        ),
    ]
