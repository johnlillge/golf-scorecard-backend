from .models import Round, Score
from .serializers import RoundSerializer, ScoreSerializer
from rest_framework import viewsets
from rest_framework import permissions

class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer

    def get_queryset(self):
        queryset = Round.objects.all()
        player = self.request.query_params.get('player')
        if player is not None:
            queryset = queryset.filter(player_id=player)
        return queryset

class ScoreViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Score.objects.filter(round=self.kwargs['round_pk'])
    
    serializer_class = ScoreSerializer
