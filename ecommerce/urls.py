from ecommerce import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login-register/', views.login_register_user, name='login-register'),
    url(r'login/$', views.login_user, name='login'),
    url(r'logout/$', views.logout_user, name='logout'),
    url(r'register/$', views.register_user, name='register'),
    url(r'^get-listings/$', views.real_query_item_listings, name='listings'),
    url(r'^get-books/$', views.real_query_books, name='books'),
    url(r'^get-test-papers/$', views.query_test_papers, name='query_test_papers'),
    url(r'^add-new-items/$', views.addnewitem, name='addnewitem'),
    url(r'^sell-books/$', views.sell_books, name="sell_books"),
    url(r'^buy-books/$', views.buy_books, name="buy_books"),
    url(r'^user-dashboard/$', views.query_user_dashboard, name='query_user_dashboard'),
    url(r'^admin-dashboard/$', views.query_admin_dashboard, name='query_admin_dashboard'),
    url(r'^add-to-cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove-from-cart/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^place-order/$', views.place_order, name='place_order'),
    # url(r'^item_list/$', views.item_list, name='itemlist'),
    # url(r'^(item_detail?P<id>\d+)/$', views.item_detail, name='itemdetail'),
    url(r'^cart-view/$', views.get, name='cartview'),
    # make view for admin / user dashboard for same url
    url(r'^view-book-details/$', views.view_book_details, name='book-details'),
    url(r'^add-new-listing/$', views.add_new_listing, name='add-new-listing'),
    url(r'^dashboard/$', views.show_dashboard, name="show-dashboard"),
    url(r'^view-details/$', views.view_listing_details, name="view-details"),
    url(r'^test-papers/$', views.test_papers, name="view-details"),
]
