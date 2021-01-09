import os
import pprint
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

#Fake pop script
import random
from first_app.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    Top = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    Top.save()
    return Top



def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        Webpg = Webpage.objects.get_or_create(topic = top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=Webpg,date=fake_date)[0]
        Webpg.save()
        acc_rec.save()
def populate_person(N=5):
    for entry in range(N):
        person = User.objects.get_or_create(first_name=fakegen.first_name,Last_name=fakegen.last_name,Email=fakegen.email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate_person(20)
    print("Populating Completed!")
