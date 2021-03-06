from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField("Titre et auteur du livre", max_length=128)
    description = models.TextField("Votre demande", max_length=2048,
                                   blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField("Image de couverture", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField("Note",
                                              validators=[
                                                  MinValueValidator(0),
                                                  MaxValueValidator(5)])
    headline = models.CharField("Titre de la critique", max_length=128)
    body = models.TextField("Critique", max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user', )
