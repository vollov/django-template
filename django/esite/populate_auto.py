import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esite.settings')

import django
django.setup()

from auto.models import Car

#
def add_car(make, model, km, year, color, eng, drive,trans, icolor):
    c = Car.objects.get_or_create(make=make, model=model, kilometers=km, year=year, color=color, engine_size=eng, drivetrain=drive, transmition=trans, interanl_color=icolor)


def populate():
    # car = Car(make='Acura',model='TL', kilometers=74673, year=2012, color='White', engine_size=3.7, drivetrain='AWD', transmition='MA')
    add_car('Acura', 'TL', 74673, 2012, 'White', 3.7, 'AWD','MA','White')
    add_car('Volkswagen', 'Touareg', 5344, 2015, 'Silver', 3.6, 'AWD','AU','White')
    
if __name__ == '__main__':
    print "Starting Car population script..."
    populate()
    

# def populate():
#     python_cat = add_cat('Python')
# 
#     add_page(cat=python_cat,
#         title="Official Python Tutorial",
#         url="http://docs.python.org/2/tutorial/")
# 
#     add_page(cat=python_cat,
#         title="How to Think like a Computer Scientist",
#         url="http://www.greenteapress.com/thinkpython/")
# 
#     add_page(cat=python_cat,
#         title="Learn Python in 10 Minutes",
#         url="http://www.korokithakis.net/tutorials/python/")
# 
#     django_cat = add_cat("Django")
# 
#     add_page(cat=django_cat,
#         title="Official Django Tutorial",
#         url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
# 
#     add_page(cat=django_cat,
#         title="Django Rocks",
#         url="http://www.djangorocks.com/")
# 
#     add_page(cat=django_cat,
#         title="How to Tango with Django",
#         url="http://www.tangowithdjango.com/")
# 
#     frame_cat = add_cat("Other Frameworks")
# 
#     add_page(cat=frame_cat,
#         title="Bottle",
#         url="http://bottlepy.org/docs/dev/")
# 
#     add_page(cat=frame_cat,
#         title="Flask",
#         url="http://flask.pocoo.org")
# 
#     # Print out what we have added to the user.
#     for c in Category.objects.all():
#         for p in Page.objects.filter(category=c):
#             print "- {0} - {1}".format(str(c), str(p))
# 
# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title)[0]
#         p.url=url
#         p.views=views
#         p.save()
#     return p
# 
# def add_cat(name):
#     c = Category.objects.get_or_create(name=name)[0]
#     return c

# Start execution here!
# if __name__ == '__main__':
#     print "Starting Rango population script..."
#     populate()