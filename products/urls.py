
from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ProductListView, basket_add, basket_remove, ProductSearchView

app_name = 'products'

urlpatterns = [
    path('', cache_page(30)(ProductListView.as_view()), name='index'),
    # path('', ProductListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductListView.as_view(), name='category'),
    path('page/<int:page>', ProductListView.as_view(), name='paginator'),
    path('search', ProductSearchView.as_view(), name='product_search'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

