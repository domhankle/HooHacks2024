# Generated by Django 4.1.13 on 2024-03-24 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Immunization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('up_to_date', models.BooleanField()),
                ('expires', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('refill', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(blank=True, max_length=100)),
                ('height', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service.user')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            bases=('service.user',),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('complete', models.BooleanField()),
                ('notes', models.CharField(blank=True, max_length=1000)),
                ('reason_for_visit', models.CharField(blank=True, max_length=100)),
                ('vitals', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.vitals')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service.user')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('appointments', models.ManyToManyField(blank=True, to='service.appointment')),
                ('doctors', models.ManyToManyField(blank=True, to='service.doctor')),
                ('immunizations', models.ManyToManyField(blank=True, to='service.immunization')),
                ('prescriptions', models.ManyToManyField(blank=True, to='service.prescription')),
            ],
            bases=('service.user',),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ManyToManyField(blank=True, to='service.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ManyToManyField(blank=True, to='service.doctor'),
        ),
    ]
