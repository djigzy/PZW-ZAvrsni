import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_KORISNIK = 20
NUM_REPUTACIJA = 20
NUM_KOMENTAR = 30
NUM_BLOG = 10
COMMENT_PER_BLOG = 3


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik,Reputacija,Komentar,Blog]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        posts = []
        for _ in range(NUM_KOMENTAR):
            kom = KomentarFactory()
            posts.append(kom)
                
        for _ in range(NUM_KORISNIK):
            korisnik = KorisnikFactory()

        for _ in range(NUM_REPUTACIJA):
            reputacija = ReputacijaFactory()
            
        for _ in range(NUM_KOMENTAR):
            komentar = KomentarFactory()
            
        for _ in range(NUM_BLOG):
            blog = BlogFactory()
            comment = random.choices(posts,k=COMMENT_PER_BLOG)
            blog.comment.add(*comment)