# Generated by Django 4.2.1 on 2023-06-07 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('subscriptions', '0003_stateorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='content_type',
            field=models.ForeignKey(help_text='Content type of object to be linked to the subscription', null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, help_text='The ID of the linked object', null=True),
        ),
    ]
