# Generated by Django 3.0.3 on 2020-07-29 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatedworkflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='resourcecentre',
            unique_together={('newscentre', 'journalist')},
        ),
    ]