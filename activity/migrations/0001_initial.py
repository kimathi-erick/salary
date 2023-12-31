# Generated by Django 4.2 on 2023-05-07 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Middle_Name', models.CharField(max_length=200, null=True)),
                ('Gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=200, null=True)),
                ('Id_Number', models.CharField(blank=True, max_length=200, null=True)),
                ('Phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('presentstatus', models.CharField(choices=[('Absent', 'Absent'), ('Present', 'Present')], default='Absent', max_length=200)),
                ('paystatus', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Absent', 'Absent')], default='Absent', max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.worker')),
            ],
        ),
    ]
