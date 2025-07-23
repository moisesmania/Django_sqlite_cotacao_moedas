from django.db import models

class Cotacao(models.Model):
    TIPO_CHOICES = [
        ('USD', 'Dólar'),
        ('EUR', 'Euro'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
    ]
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=20, decimal_places=8)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.valor}'
