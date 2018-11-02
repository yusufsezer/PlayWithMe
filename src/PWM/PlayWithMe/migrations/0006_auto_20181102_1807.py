# Generated by Django 2.1.1 on 2018-11-02 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlayWithMe', '0005_auto_20181102_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PlayWithMe.Game'),
        ),
        migrations.AddField(
            model_name='session',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='PlayWithMe.User'),
        ),
        migrations.AddField(
            model_name='session',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='PlayWithMe.User'),
        ),
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.CharField(help_text='ID to uniquely identify a session', max_length=60, primary_key=True, serialize=False),
        ),
    ]
