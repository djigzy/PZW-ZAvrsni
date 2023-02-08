from django.test import TestCase,SimpleTestCase, Client
from django.urls import reverse, resolve
from main.models import *
from main.views import *

# Testovi za models.py
class Testmodels(TestCase):

    def setUp(self):
        self.user = Korisnik.objects.create(
            name = "Ime",
            user_name = "Korisnicko ime",
            email = "Email",
            password = "Lozinka",
        )
        self.comment = Komentar.objects.create(
            comment = "Komentar",
            user_name = Korisnik.objects.create(
                name = "Ime",
                user_name = "Korisnicko ime2",
                email = "Email",
                password = "Lozinka",
            ),
        )
        self.reputation = Reputacija.objects.create(
            points = "1",
            user_name = Korisnik.objects.create(
                name = "Ime",
                user_name = "Korisnicko ime2",
                email = "Email",
                password = "Lozinka",
            ),
        )
        self.blog = Blog.objects.create(
            theme = "Tema bloga",
            date = "1992-02-01",
            time = "8:25",
        )

    def testKorisnikName(self):
        self.assertEquals(self.user.name,"Ime")
    
    def testKomentarName(self):
        self.assertEquals(self.comment.user_name.user_name,"Korisnicko ime2")

    def testReputacijaName(self):
        self.assertEquals(self.reputation.user_name.user_name,"Korisnicko ime2")
    
    def testBlogTime(self):
        self.assertEquals(self.blog.time,"8:25")






# Testovi za views.py
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_link = reverse('main:index')
        self.reputacija_link = reverse('main:reputations')

    def test_index_GET(self):
        client = Client()

        response = client.get(self.index_link)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_reputations_GET(self):
        client = Client()

        response = client.get(self.reputacija_link)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/reputacija_list.html')




# Testovi za urls.py
class TestUrls(SimpleTestCase):

    def test_is_resolved_index(self):
        url = reverse('main:index')
        self.assertEquals(resolve(url).func, index)

    def test_is_resolved_korisnik(self):
        url = reverse('main:users')
        self.assertEquals(resolve(url).func.view_class, KorisnikList)

    def test_is_resolved_reputacija(self):
        url = reverse('main:reputations')
        self.assertEquals(resolve(url).func.view_class, ReputacijaList)
       
    def test_is_resolved_register(self):
        url = reverse('main:register')
        self.assertEquals(resolve(url).func, register_request)

    def test_is_resolved_login(self):
        url = reverse('main:login')
        self.assertEquals(resolve(url).func, login_request)
        
    def test_is_resolved_novaReputacija(self):
        url = reverse('main:formaNovaReputacija')

        self.assertEquals(resolve(url).func, novaReputacija)


