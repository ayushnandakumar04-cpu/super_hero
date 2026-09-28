from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from batman.models import Superhero
from batman_v2.serializers import SuperheroSerializer
from rest_framework.response import Response
# Create your views here.
class SuperheroListCreateview(APIView):

    def get(self,request):
        qs=Superhero.objects.all()
        serializer_instants=SuperheroSerializer(qs)
        return Response(data=serializer_instants.data)
    
    def post(self,request):
        form_data=request.data
        Superhero.objects.create(
            name=form_data.get("name"),
            power=form_data.get("power"),
            team=form_data.get("team"),
            age=form_data.get("age"),
            real_name=form_data.get("real_name")
        )
        return Response(data=
                        {"message":"created"}
        )

class SuperheroListRetrieveview(APIView):
    def get(self,request,pk=None):
        qs=Superhero.objects.get(id=pk)
        serializer_instance=SuperheroSerializer(qs)
        return Response(data=serializer_instance.data)   