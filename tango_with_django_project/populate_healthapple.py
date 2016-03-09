import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from healthapple.models import Category, Page, Person

def populate():
	fever_cat = add_cat('Fever') 
	
	add_page(cat = fever_cat,
		title="About Fever",
		summary = "This is about fever",
		url = "https://en.wikipedia.org/wiki/Fever",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	add_page(cat = fever_cat,
		title="How to cure fever",
		summary = "This is about how to cure fever",
		url = "http://www.wikihow.com/Cure-a-Fever-at-Home",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
	
	add_page(cat = fever_cat,
		title="Fever Symptomps",
		summary = "This is about symptoms of fever",
		url = "http://www.nhs.uk/Conditions/Scarlet-fever/Pages/Symptoms.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	AIDS_cat = add_cat('AIDS')
	
	add_page(cat = AIDS_cat,
		title="About AIDS",
		summary = "This is about AIDS",
		url = "http://www.avert.org/about-hiv-aids/what-hiv-aids",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
	add_page(cat = AIDS_cat,
		title="AIDS symptoms",
		summary = "Symptoms of AIDS",
		url = "http://www.nhs.uk/Conditions/HIV/Pages/Symptomspg.aspx",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
	
	add_page(cat = AIDS_cat,
		title="Cure AIDS",
		summary = "This how to cure AIDS",
		url = "http://www.cureaidsreport.org",
		flesch_score=0,
		sentiment_score=0,
		subjectivity_score=0)
		
def add_page(cat, title, summary, url, flesch_score, sentiment_score, subjectivity_score):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.summary = summary
    p.url=url
    p.flesch_score = flesch_score
    p.sentiment_score = sentiment_score
    p.subjectivity_score = subjectivity_score
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_user(user):
	u = Person.objects.get_or_create(user=user)[0]
	u.save()
	return u

# Start execution here!
if __name__ == '__main__':
    print "Starting HealthApple population script..."
    populate()
