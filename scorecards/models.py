from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from authentication.models import CustomUser

class Round(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rounds')
    time_finished = models.DateTimeField(default=timezone.now)
    total_score = models.IntegerField()

    def __str__(self):
        return f"{self.player} {self.time_finished}"

class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='scores')
    hole_num = models.IntegerField()
    hole_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

    def __str__(self):
        return f"{self.hole_num} {self.round}"
