# Generated by Django 3.1.4 on 2020-12-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_auto_20201225_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(default='', upload_to='foto/%d/%m/%Y'),
            preserve_default=False,
        ),
    ]