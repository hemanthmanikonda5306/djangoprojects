from genericrouterapp.models import Groute
from rest_framework.serializers import ModelSerializer

class Gr_serializers(ModelSerializer):
    class Meta:
        model = Groute
        fields = '__all__'
