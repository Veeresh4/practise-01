# Generated by Django 4.2 on 2023-05-04 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_pet_person_name_remove_vehicle_pet_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pet_name',
        ),
        migrations.AddField(
            model_name='pet',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='app.vehicle'),
        ),
        migrations.AddField(
            model_name='pet',
            name='person_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.person'),
        ),
    ]