# Generated by Django 4.1.4 on 2023-09-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0002_proadd_alter_model_seller_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_byer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('photo', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]