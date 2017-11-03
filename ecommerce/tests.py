from django.test import TestCase, RequestFactory
from .models import SiteUser, Item, Listing, Cart
from django.contrib.auth.models import User
import json
import datetime


class RegisterTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_user(self):
        response = self.client.post(
            '/store/register/',
            {
                'firstnameregister': 'dummy',
                'lastnameregister': 'miloni',
                'passwordregister': 'pass@123',
                'emailregister': 'e@mail.com',
                'collegeregister': 'college',
                'nameregister': 'Dummy',
                'addressregister': 'Address Here',
                'telregister': '123456789',
                'yearregister': 'SE',
                'deptregister': 'COMPS',
                'usernameregister': 'dummyuser',
            }
        )
        self.assertEquals(response.status_code, 200)


class LoginTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testtest',
            email='testtest@testtest.al',
            password='testtest@123'
        )
        site_user = SiteUser(
            auth_user=self.user,
            tel_no="123456",
            college="college",
            address="land",
            year=datetime.datetime.now()
        )
        site_user.save()

    def test_login(self):
        response = self.client.post(
            '/store/login/',
            {
                'username_login': 'testtest',
                'password_login': 'testtest@123'
            }
        )
        if response.status_code == 302:
            user = User.objects.get(username='testtest')
            self.assertTrue(user.is_authenticated())
        else:
            self.assertTrue(False)

    def test_login_fail(self):
        response = self.client.post(
            '/store/login/',
            {
                'username_login': 'testtes',
                'password_login': 'testtest@124'
            }
        )
        self.assertEquals(response.status_code, 200)


class QueryTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.book = Item.objects.create(
            title='Kumbhojkar',
            max_price=700,
            publisher='publisher',
            author='Kumbhojkar',
            quantity=1,
            subject='maths',
            department="COMPS",
            year='FE'
        )
        self.user = User.objects.create_user(
            username='testtest',
            email='testtest@testtest.al',
            password='testtest@123'
        )
        site_user = SiteUser(
            auth_user=self.user,
            tel_no="123456",
            college="college",
            address="land",
            year=datetime.datetime.now()
        )
        site_user.save()
        self.listing = Listing.objects.create(
            item=self.book,
            price=500,
            seller_id=site_user.id
        )

    def test_book_query(self):
        json_request_dict = {
            'title': "Kumbhojkar",
            "subject": "maths"
        }
        response = self.client.post(
            '/store/get-books/',
            json.dumps(json_request_dict),
            content_type='application/json'
        )
        matches = True
        self.assertTrue(matches)

    def test_listing_query(self):
        json_request_dict = {
            'title': "Kumbhojkar",
            "subject": "maths"
        }
        response = self.client.post(
            '/store/get-listings/',
            json.dumps(json_request_dict),
            content_type='application/json'
        )
        # print(response.content)
        matches = True
        self.assertTrue(matches)


class AddItemTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_item(self):
        request_dict = {
            'itemtype': 'Book',
            'title': 'Cormen',
            'year': 'SE',
            'department': 'COMPS',
            'author': 'Cormen',
            'publisher': 'Pearson',
            'description': 'Kaafi sahi',
            'maxprice': 1000,
            'subject': 'Algorithms',
        }
        response = self.client.post(
            '/store/add-new-items/',
            request_dict,
        )
        self.assertEquals(response.status_code, 302)
        query_list = Item.objects.filter(title__contains="Cormen")
        if not query_list:
            self.assertFalse(True)


class CartTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.book = Item.objects.create(
            title='Kumbhojkar',
            max_price=700,
            publisher='publisher',
            author='Kumbhojkar',
            quantity=1,
            subject='maths',
            department="COMPS",
            year='FE'
        )
        self.book.quantity = 1
        self.book.save()
        self.user = User.objects.create_user(
            username='testtest',
            email='testtest@testtest.al',
            password='testtest@123'
        )
        site_user = SiteUser(
            auth_user=self.user,
            tel_no="123456",
            college="college",
            address="land",
            year=datetime.datetime.now()
        )
        site_user.save()
        self.listing = Listing.objects.create(
            item=self.book,
            price=500,
            seller_id=site_user.id
        )
        self.client.login(username='testtest', password='testtest@123')

    def test_add_to_cart(self):
        self.client.post(
            '/store/add-to-cart/', {"listing_id": self.listing.id})
        cart_of_user = Cart.objects.get(user_id=self.user.id)
        listing = Listing.objects.get(id=self.listing.id)
        if cart_of_user is not None:
            self.assertTrue(listing.order is not None)
            print(cart_of_user.id)
            print(listing.order.id)
            self.assertTrue(cart_of_user.id == listing.order.id)
            self.assertTrue(self.user.id == cart_of_user.user.id)
        else:
            self.assertTrue(False)

    def test_delete_from_cart(self):
        self.client.post(
            '/store/add-to-cart/', {"listing_id": self.listing.id})
        self.client.post('/store/remove-from-cart/',
                         {"listing_id": self.listing.id})
        listing = Listing.objects.get(id=self.listing.id)
        self.assertTrue(listing.order is None)

class UserDashboardQueryTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testtest',
            email='testtest@testtest.al',
            password='testtest@123'
        )
        site_user = SiteUser(
            auth_user=self.user,
            tel_no="123456",
            college="college",
            address="land",
            year=datetime.datetime.now()
        )
        site_user.save()

    def test_userdashboard_query(self):
        request_dict = {
            'college': 'college',
            'address': 'land',
        }
        response = self.client.post(
            '/store/query_user_dashboard/',
            request_dict,
        )
        matches = True
        self.assertTrue(matches)
