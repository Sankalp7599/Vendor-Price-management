from django.conf.urls import url
from BRMapp import views

urlpatterns =[
url('view-products',views.viewProducts),
url('edit-product',views.editProduct),
url('delete-product',views.deleteProduct),
url('search-product',views.searchProduct),
url('new-product',views.NewProduct),
url(r'^add',views.add),
url('search',views.search),
url('edit',views.edit),
url('login',views.userLogin),
url('logout',views.userLogout),
]
