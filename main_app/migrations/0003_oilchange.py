# Generated by Django 4.1.2 on 2022-10-17 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_aftermarket'),
    ]

    operations = [
        migrations.CreateModel(
            name='OilChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Oil Change Date')),
                ('change', models.CharField(choices=[('OIL', 'Oil'), ('OIF', 'Oil and Filter'), ('OFF', 'Oil, Filter, and Fuses')], default='OIL', max_length=3)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
