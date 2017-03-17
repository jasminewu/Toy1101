from django.db import models

class Moment(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000, default='')
    # photo = models.URLField( max_length=100, blank=True, default='')
    photo = models.CharField( max_length=100, blank=True, default='')

    user_id = models.ForeignKey('auth.User')
    class Meta:
        ordering = ('id',)
