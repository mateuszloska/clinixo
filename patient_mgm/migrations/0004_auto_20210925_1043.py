# Generated by Django 3.2.7 on 2021-09-25 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient_mgm', '0003_alter_contactprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactprofile',
            name='contact_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('physician', 'Physician'), ('other-stuff', 'Other-Stuff')], default='patient', max_length=20),
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='first_name',
            field=models.CharField(default='first_name', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactprofile',
            name='last_name',
            field=models.CharField(default='last_name', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactprofile',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contact_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]