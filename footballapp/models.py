from django.db import models

# Create your models here.
class Player(models.Model):
    Name = models.CharField(max_length=100, default='')
    Age = models.IntegerField(default='')
    Club = models.TextField()
    # MY_CHOICES=(('Forward'),('Midfield'),('Defender'),('Goalkeeper'))
    Position = models.CharField(max_length=100)
    Birthdate = models.DateField(max_length=100)
    Nationality = models.CharField(max_length=100)
    InfoId = models.ForeignKey('Team', related_name='Player_id', on_delete=models.CASCADE, default='')
    class Meta:
        ordering = ('Name',)
    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)

class Team(models.Model):
    TeamName = models.CharField(max_length=100, default='')
    League = models.CharField(max_length=100, default='')
    # Age = models.IntegerField(default='')
    # Club = models.TextField()
    # Position = models.TextField()
    # Birthdate = models.DateField(max_length=100)
    # Nationality = models.CharField(max_length=100)
    class Meta:
        ordering = ('TeamName',)
    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)
