from django.shortcuts import render
from rest_framework.views import APIView
from batman.models import Superhero
from rest_framework.response import Response
# Create your views here.
class SuperheroListCreateView(APIView):
    def get(self,request):
        qs=Superhero.objects.all().values()
        SH_list=list(qs)
        return Response(data=SH_list)
    def post(self,request):
        form_data=request.data
        Superhero.objects.create(
            name=form_data.get("name"),
            power =form_data.get("power"),
            age=form_data.get("age"),
            city=form_data.get("city"),
            team=form_data.get("team"),
            real_name=form_data.get("real_name")
        )
        
        return Response(data=
                        {"message":"created"}
                    )
class SuperheroListRetrieveView(APIView):
    def get(self,request,pk=None):
        qs=Superhero.objects.filter(id=pk).values()
        Sp_list = list(qs)
        return Response(data=Sp_list)
    def delete(self,request, pk):
             sp= Superhero.objects.get(id=pk)
             sp.delete()

             sp_list= {
                "Message": "Deleted successfully"
            }
             return Response(data=sp_list)
    def put(self,request,pk):
        form_data =(request.data)
        super = Superhero.objects.get(id=pk)
        Superhero.objects.create(
                      name=form_data.get("name"),
                      power =form_data.get("power"),
                      age=form_data.get("age"),
                      city=form_data.get("city"),
                      team=form_data.get("team"),
                      real_name=form_data.get("real_name")
            )
        
        response_data={
                "Message": "Movie updated successfully"
            }
        return Response(data=response_data)
            