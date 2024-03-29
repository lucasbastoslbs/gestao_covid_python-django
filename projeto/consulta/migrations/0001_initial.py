# Generated by Django 3.0.4 on 2023-04-06 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Use dd/mm/aaaa', max_length=10, verbose_name='Data da triagem ')),
                ('hora', models.TimeField(help_text='Use hh:mm', max_length=10, verbose_name='Hora da triagem ')),
                ('paciente', models.CharField(help_text='* indica campos obrigatórios', max_length=100, verbose_name='Informe o nome completo do paciente *')),
                ('prescricao', models.CharField(help_text='* indica campos obrigatórios', max_length=200, verbose_name='Prescrição para o paciente *')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medicamento', to='medicamento.Medicamento', verbose_name='Medicamento para a consulta')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medico', to=settings.AUTH_USER_MODEL, verbose_name='Responsável pela triagem *')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
                'ordering': ['-data', '-hora', 'paciente'],
                'unique_together': {('data', 'hora', 'paciente')},
            },
        ),
    ]
