from django.db import models

class Car(models.Model):
    AUTOMATIC = 'AU'
    MANUAL = 'MA'
    OTHER = 'OT'
    
    FWD = 'FWD'
    AWD = 'AWD'
    RWD = 'RWD'
    
    # TRANSMISSION: Automatic,MANUAL,other
    TRANSMISSION_CHOICE = (
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
        (OTHER, 'Other'),
    )

    # drivetrain: FWD, AWD, RWD, other
    DRIVETRAIN_CHOICE = (
        (FWD, 'Front wheel drive (FWD)'),
        (AWD, 'All wheel drive (AWD)'),
        (RWD, 'Rear wheel drive (RWD)'),
        (OTHER, 'Other'),
    )
    
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    kilometers = models.IntegerField(default=0)
    year = models.IntegerField(default=2000)
    engine_size = models.DecimalField(default=0.0,max_digits=3, decimal_places=1)
    
    drivetrain = models.CharField(max_length=3,
                                      choices=DRIVETRAIN_CHOICE,
                                      default=FWD)
    
    transmition = models.CharField(max_length=2,
                                      choices=TRANSMISSION_CHOICE,
                                      default=AUTOMATIC)
    
    color = models.CharField(max_length=20)
    interanl_color = models.CharField(max_length=20)

    def __unicode__(self):
        return self.make
