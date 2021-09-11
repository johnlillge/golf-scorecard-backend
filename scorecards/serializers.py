from rest_framework import serializers
from .models import Round, Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'hole_num', 'hole_score']

class RoundSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Round
        fields = ['id', 'player', 'time_finished', 'total_score', 'scores']

    def create(self, validated_data):
        scores_data = validated_data.pop('scores')
        round = Round.objects.create(**validated_data)
        for score_data in scores_data:
            Score.objects.create(round=round, **score_data)
        return round

    def update(self, instance, validated_data):
        scores_data = validated_data.pop('scores')
        scores = (instance.scores).all()
        scores = list(scores)
        instance.total_score = validated_data.get('total_score', instance.total_score)
        instance.save()
        for score_data in scores_data:
            score = scores.pop(0)
            score.hole_num = score_data.get('hole_num', score.hole_num)
            score.hole_score = score_data.get('hole_score', score.hole_score)
            score.save()
        return instance
