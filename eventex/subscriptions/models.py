from django.db import models


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)    
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscricao'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

    def test_paid_default_to_False(self):
        """"By default paid must be False"""
        self.assertEqual(False,self.obj.paid)
