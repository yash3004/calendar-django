from django.db import models
from django.urls import reverse
import uuid




class Event(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teacher = models.CharField(max_length=100)

   

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
class Booking(models.Model):
    student = models.CharField(max_length=100)
    # id = models.UUIDField(default=uuid.uuid4 , primary_key= True , editable=False , unique=True)
    lecture  = models.CharField(max_length=150)