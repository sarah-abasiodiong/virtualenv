from django.test import TestCase
from django.urls import reverse, resolve
from .views import home_page, about_us, contact_us

# Create your tests here.
class ViewTestCase(TestCase):

    def test_home_view(self):
        res = resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.content, "Welcome to MulZact Store")
        self.assertEquals(res.func, home_page)


    def test_about_view(self):
        res = resolve(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.content, b"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi possimus saepe recusandae delectus facere commodi earum nisi cum, exercitationem iusto. Eaque esse omnis quia veritatis labore facere delectus deserunt quis?")
        self.assertEquals(res.func, about_us)


    def test_contact_view(self):
        res = resolve(reverse("contact"))
        response = self.client.get(reverse("contact"))
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.content, b"<p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum velit nostrum, earum in deleniti nam quo rerum architecto ad, quasi corrupti. Nostrum quod nihil temporibus dolore iure nemo optio reprehenderit?</p>")
        self.assertEquals(res.func, contact_us)


# Create your tests here.
