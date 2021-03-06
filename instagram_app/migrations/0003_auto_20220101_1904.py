# Generated by Django 3.2.10 on 2022-01-02 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_app', '0002_auto_20220101_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram_app.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram_app.post'),
        ),
    ]
