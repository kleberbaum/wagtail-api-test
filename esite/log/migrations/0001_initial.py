# Generated by Django 2.2.9 on 2020-04-29 14:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workpackage',
            fields=[
                ('name', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('new', 'Workpackage has not been started'), ('ongoing', 'Workpackage is in progress'), ('waiting', 'Workpackage cannot be continued due to dependencies'), ('review', 'Workpackage is under review'), ('fin', 'Workpackage is complted and reviewed')], default='new', max_length=32)),
                ('durration', models.DurationField(null=True)),
                ('realtime', models.DurationField(default='00:00:00', null=True)),
                ('sid', models.CharField(default='0', max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{1,3}$')])),
                ('did', models.CharField(default='0.0', max_length=7, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{1,3}\\.\\d{1,3}$')])),
                ('pid', models.CharField(default='0.0.0', max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='ID doesnt comply', regex='^\\d{1,3}\\.\\d{1,3}.\\d{1,3}$')])),
                ('start', models.TimeField(null=True)),
                ('end', models.TimeField(null=True)),
                ('assoc_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Associated User')),
            ],
        ),
    ]