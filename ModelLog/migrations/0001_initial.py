# Generated by Django 4.2.4 on 2023-09-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                (
                    'operation',
                    models.CharField(
                        choices=[('arbitrary-image-stylization-v1-256/2', 'neural-style-transfer-v2'),
                                 ('image-super-resolution-SRRestNet-SRGAN', 'image-super-resolution-GANs')],
                        max_length=255
                    )
                ),
            ],
        ),
    ]