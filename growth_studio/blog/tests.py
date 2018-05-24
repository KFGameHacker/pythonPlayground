from django.test import TestCase

# Create your tests here.
class BlogpostListTest(TestCase):
    def setUP(self):
        self.user = User.objects.create_user(username='arthas',email='arthas@kevin.com',password='arthas')
    
    def def test_blog_list_page(self):
        Blog.objects.Create(title='hello',author=self.user,slug='this_is_a_test',body='This is a blog',posted=datetime.now())
        response = self.client.get('/blog/')
        self.assertIn(b'This is a blog',response.content)

class HomepageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdri