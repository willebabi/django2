from django.forms import ModelForm
from .models import Transacao

class transForm (ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','obs','categoria'] 