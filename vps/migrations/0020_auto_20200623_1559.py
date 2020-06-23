# Generated by Django 2.2.5 on 2020-06-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0019_auto_20200623_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_topic',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='置顶'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pid',
            field=models.IntegerField(default=0, verbose_name='PID'),
        ),
    ]