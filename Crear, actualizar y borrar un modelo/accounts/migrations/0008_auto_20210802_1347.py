# Generated by Django 3.2 on 2021-08-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categorie',
            new_name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]