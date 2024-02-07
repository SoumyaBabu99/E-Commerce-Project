# Generated by Django 4.1.4 on 2023-09-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_model_byer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proadd',
            name='ptype',
        ),
        migrations.AddField(
            model_name='proadd',
            name='p_type',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('jewellery', 'Jewellery'), ('electronic', 'Electronic')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proadd',
            name='photo',
            field=models.FileField(upload_to='ecommerce_app/static'),
        ),
    ]