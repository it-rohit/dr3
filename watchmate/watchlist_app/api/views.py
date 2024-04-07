from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .. models import Movie
from . serializer import MovieSerializer

##list of movies and create
class Movies_list(APIView):
    def get(self,request):
        movie = Movie.objects.all()
        serializer1 = MovieSerializer(movie,many=True)
        return Response (serializer1.data,status=status.HTTP_200_OK)
    
    def post (self,request):
        data1=request.data
        serializer1 = MovieSerializer(data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data,status=status.HTTP_201_CREATED)
        else:
            print("hai")
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
        

###update delete
class Movie_Update_Delete(APIView):
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response ({"msg":"no Movie found"},status = status.HTTP_404_NOT_FOUND)

        serializer1 = MovieSerializer(movie)                
        return Response (serializer1.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk):

        movie = Movie.objects.get(pk=pk)
        data1=request.data
        serializer1=MovieSerializer(instance=movie,data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response (serializer1.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete (self,request,pk):
        movie= Movie.objects.get(pk=pk)
        movie.delete()
        return Response ({"msg":"movie sucessfully deleted"},status=status.HTTP_204_NO_CONTENT)
    

