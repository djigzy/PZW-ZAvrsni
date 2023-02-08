from django.db import models

class Korisnik(models.Model):

    name = models.CharField("Ime", max_length=64, null=True)
    user_name = models.CharField("Korisnicko ime", max_length=64, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    password = models.CharField("Lozinka", max_length=20, null=True)
    
    def __str__(self):
        return self.user_name


class Reputacija(models.Model):
    points = models.IntegerField("Reputacija", null=True)
    user_name = models.OneToOneField(Korisnik, on_delete = models.CASCADE,default = None, blank=True, null=True)
    

class Komentar(models.Model):
    comment = models.CharField("Komentar", max_length= 500, blank=True, null=True)
    user_name = models.ForeignKey(Korisnik, on_delete = models.CASCADE,default = None, blank=True, null=True)
    
    def __str__(self):
        return self.comment
    
class Blog(models.Model):
    theme = models.CharField("Tema bloga", max_length= 50,blank=True, null=True )
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    comment = models.ManyToManyField(Komentar)