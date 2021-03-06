# Generated by Django 3.2.7 on 2021-09-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_mgm', '0006_alter_contactprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactprofile',
            name='roles',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactprofile',
            name='contact_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('physician', 'Physician'), ('manager', 'Manager'), ('reception', 'Reception'), ('other-stuff', 'Other-Stuff')], default='patient', max_length=20),
        ),
    ]
