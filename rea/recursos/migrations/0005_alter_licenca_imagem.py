# Generated by Django 4.0.6 on 2022-08-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0004_alter_licenca_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenca',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
    ]
