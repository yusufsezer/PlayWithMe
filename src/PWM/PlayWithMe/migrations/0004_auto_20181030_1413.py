# Generated by Django 2.1.1 on 2018-10-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlayWithMe', '0003_auto_20181030_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PlayWithMe.Game'),
        ),
        migrations.AddField(
            model_name='user',
            name='platforms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PlayWithMe.Platform'),
        ),
        migrations.AddField(
            model_name='user',
            name='sessions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PlayWithMe.Session'),
        ),
    ]
