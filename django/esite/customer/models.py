from django.db import models
import uuid

class Customer(models.Model):
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    name = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    sin = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=125, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
