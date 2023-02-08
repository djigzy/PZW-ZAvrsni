import factory
from factory.django import DjangoModelFactory

from main.models import *
import factory.fuzzy

import random


class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    name = factory.Faker("first_name")
    user_name = factory.Faker("first_name")
    email = factory.Faker("free_email")
    password = factory.fuzzy.FuzzyInteger(1000,999999)

class ReputacijaFactory(DjangoModelFactory):
    class Meta:
        model = Reputacija

    points = factory.fuzzy.FuzzyInteger(0,999999)
    user_name = factory.Iterator(Korisnik.objects.all())

class KomentarFactory(DjangoModelFactory):
    class Meta:
        model=Komentar

    comment = factory.Faker("sentence",nb_words=5)
    user_name = factory.SubFactory(KorisnikFactory)

class BlogFactory(DjangoModelFactory):
    class Meta:
        model=Blog

    theme = factory.Faker("sentence",nb_words=5)
    date = factory.Faker("date_time")
    time = factory.Faker("time")