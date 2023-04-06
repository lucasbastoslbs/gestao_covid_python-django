from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
#from ..usuario.models import MedicoAtivoManager

from utils.gerador_hash import gerar_hash
    
class Consulta(models.Model):
    # medicos_ativos = MedicoAtivoManager()
    # medico = models.CharField('Selecione medico responsavel', choices=medicos_ativos, max_length=50)
    medico = models.ForeignKey('usuario.Usuario', verbose_name= 'Responsável pela triagem *', on_delete=models.PROTECT, related_name='medico')
    data = models.DateField('Data da triagem ', max_length=10, help_text='Use dd/mm/aaaa')
    hora = models.TimeField('Hora da triagem ', max_length=10, help_text='Use hh:mm')
    paciente = models.CharField('Informe o nome completo do paciente *', max_length=100, help_text= '* indica campos obrigatórios')
    prescricao = models.CharField('Prescrição para o paciente *', max_length=200, help_text= '* indica campos obrigatórios')
    medicamento = models.ForeignKey('medicamento.Medicamento', verbose_name= 'Medicamento para a consulta', on_delete=models.PROTECT, related_name='medicamento')
    
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    class Meta:
        ordering            =   ['-data', '-hora', 'paciente']
        verbose_name        =   ('consulta')
        verbose_name_plural =   ('consultas')
        unique_together     =   [['data','hora','paciente']] #erro quando adiciona mesmos dados

    def __str__(self):
        return "Paciente: %s. Data/hora: %s - %s ." % (self.paciente, self.data, self.hora)

    def save(self, *args, **kwargs):
        self.paciente = self.paciente.upper()        
        if not self.slug:
            self.slug = gerar_hash()
        super(Consulta, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('consulta_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('consulta_delete', args=[str(self.id)]) 