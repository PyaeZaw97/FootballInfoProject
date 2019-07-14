from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from footballapp.models import Player, Team
from footballapp.serializers import PlayerSerializer, TeamSerializer
from rest_framework import mixins
from rest_framework import generics


class PlayerList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        footballapp = Player.objects.all()
        serializer = PlayerSerializer(footballapp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PlayerList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        footballapp = Team.objects.all()
        serializer = TeamSerializer(footballapp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeamList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        playball = self.get_object(pk)
        serializer = PlayerSerializer(playball)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        playball = self.get_object(pk)
        serializer = PlayerSerializer(playball, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        playball = self.get_object(pk)
        playball.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlayerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        playboy = self.get_object(pk)
        serializer = TeamSerializer(playboy)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        playboy = self.get_object(pk)
        serializer = TeamSerializer(playboy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        playboy = self.get_object(pk)
        playboy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer