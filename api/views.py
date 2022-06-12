from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movies, Ratings
from .serializers import MoviesSerializer, RatingsSerializer, UserSerializer

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MoviesViewset(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST', ])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:
            #data = request.data
            movie = Movies.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            #print(user)
            
            try:
                current_rating = Ratings.objects.get(movie=movie.id,user=user.id)
                current_rating.stars = stars
                current_rating.save()
                serializer = RatingsSerializer(current_rating, many=False)
                response = {'message': 'Rating updated', 'response':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                new_rating = Ratings.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingsSerializer(new_rating,many=False)
                response = {'message': 'Rating created', 'response':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':'bad request please provide stars for the movie'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingsViewset(viewsets.ModelViewSet):
    serializer_class = RatingsSerializer
    queryset = Ratings.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        response = {'message':'You can not create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message':'You can not update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
