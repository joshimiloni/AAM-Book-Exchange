from django.db import models
# from . import model_enums as enums
from django.conf import settings
from django.db import models
from django.contrib.sessions.models import Session
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import utils
import datetime
from django.contrib.auth.models import User

# NOTE: remember to implement choices
# http://blog.richard.do/index.php/2014/02/how-to-use-enums-for-django-field-choices/
YEAR_CHOICES = (
    ('FE', 'FIRST_YEAR'),
    ('SE', 'SECOND_YEAR'),
    ('TE', 'THIRD_YEAR'),
    ('BE', 'FOURTH_YEAR'),
)

DEPT_CHOICES = (
    ('COMPS', 'COMPUTERS'),
    ('IT', 'INFORMATION_TECHNOLOGY'),
    ('ELEX', 'ELECTRONICS'),
    ('EXTC', 'ELECTRONICS_TELECOMM'),
    ('MECH', 'MECHANICAL'),
    ('PROD', 'PRODUCTION'),
    ('BIO', 'BIOMEDICAL'),
)

ORDER_STATUS_CHOICES = (
    ('CRT', 'CART'),
    ('PND', 'PENDING'),
    ('DSP', 'DISPATCHED'),
)


class Item(models.Model):
    itemtype = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    subject = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    department = models.CharField(
        max_length=6, null=True, choices=DEPT_CHOICES
    )
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)

    # If we want to store when the model was added(created), and when seller updates quantity
    # created = models.DateTimeField(auto_now_Add = True)
    # updated = models.DateTimeField(auto_now = True)

    def get_json(self):
        dict_self = {
            'title': self.title,
            'max_price': self.max_price,
            'publisher': self.publisher,
            'author': self.author,
            'subject': self.subject,
            'department': self.department
        }
        json_self = json.dumps(dict_self)
        return json_self


class SiteUser(models.Model):
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tel_no = models.CharField(max_length=20)
    college = models.CharField(max_length=50)
    year = models.DateField()
    department = models.CharField(
        max_length=6, null=True, choices=DEPT_CHOICES
    )
    address = models.CharField(max_length=100)

    def get_json(self):
        dict_self = {
            'tel_no': self.tel_no,
            'college': self.college,
            'address': self.address,
            'year': utils.get_year_string(self.year),
            'department': self.department
        }
        return json.dumps(dict_self)


class Listing(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    price = models.IntegerField()
    order = models.ForeignKey('Cart', null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey('SiteUser', on_delete=models.CASCADE)

    def get_json(self):
        dict_self = {
            'price': self.price,
            'order': self.order,
            'item': self.item.get_json(),
            'seller': self.seller.get_json()
        }
        return json.dumps(dict_self)


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #    user = models.ForeignKey('SiteUser', on_delete=models.CASCADE)
    session = models.ForeignKey(Session)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
  
    # quantity of number of items in cart from listing
    quantity = models.PositiveIntegerField(default=0)
    addtocart_date_time = models.DateTimeField()
    # subtotal = models.DecimalField(max_digits=50, decimal_places=2, null=True) #listing price
    order_status = models.CharField(max_length=20, default="pending in cart")

    # def get_json(self):
        # dict_self = {
            # 'item': self.item.get_json(),
            # 'user': self.user.get_json(),
            # 'quantity': self.quantity,
            # 'addtocart_date_time': self.addtocart_date_time,
            # # 'subtotal': self.subtotal,
            # # 'updated': self.updated,
            # 'order': self.order.get_json(),
        # }
        # return json.dumps(dict_self)


    # def __str__(self):
        # return str(self.id)

        # # @login_required
        # # def add_to_cart(request,book_id):
        # # book = get_object_or_404(Item, pk=book_id)
        # # created is a boolean specifying whether a new object was created.
        # # cart,created = Requests.objects.get_or_create(user=request.user, active=True)
        # # order,created = Order.objects.get_or_create(book=book,cart=cart)
        # # order.quantity += 1
        # # order.save()
        # # messages.success(request, "Cart updated!")
        # # return redirect('cart')
