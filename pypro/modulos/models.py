from django.db import models
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=46)
    publico = models.TextField()
    descricao = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
