from rest_framework.serializers import ModelSerializer
from viewsetcrudapp.models import View_crud

class View_serializers(ModelSerializer):
    class Meta:
        model = View_crud
        fields = '__all__'