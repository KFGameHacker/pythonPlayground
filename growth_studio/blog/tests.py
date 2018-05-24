from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class BlogpostListTest(TestCase):
    def setUP(self):
        self.user = User.objects.create_user(username='arthas',email='arthas@kevin.com',password='arthas')
    
    def def test_blog_list_page(self):
        Blog.objects.Create(title='hello',author=self.user,slug='this_is_a_test',body='This is a blog',posted=datetime.now())
        response = self.client.get('/blog/')
        self.assertIn(b'This is a blog',response.content)

class BlogDetailTest(TestCase):
    def test_not_found_blog(self):
        response = self.client.get('/blog/xxxx.html')
        self.assertEqual(404,response.status_code)

class HomepageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.user = User.objects.create_user(username='arthas',email='arthas@qq.com',password='arthas')
        super(HomepageTestCase,self).setUP()
    
    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase,slef).tearDown()
    
    def test_should_goto_blog_page_from_homepage(self):
        Blog.objects.create(title='hello',author=self.user,slug='this_is_a_test',body='This is blog detail',posted=datetime.now())
        self.selenium.get(
            '%s%s' % (self.live_server_url,"/")
        )
        self.selenium.find_element_by_link_text('博客').click()
        self.assertIn("This is blog detail",self.selenium.page_source)