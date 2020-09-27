
from django.urls import path
from .views import BooksListView, BooksDetailView, BookCheckoutView, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]

"""At first i imported 'path' module from django.url library which we will use for url routing, 
then i imported all the class based views here which we created in views.py file, 
then in urlpatterns section im telling django at which location or url which webpage should work.

For BookListView.as_view() i used empty quotation marks -> '' what it does ? 
it tells django that on the very first page work as per the BookListView class
and then i choose a reference name for this url as 'list' and mentioned it inside name.

Next is BookDetailView which will be loaded after the BookListView class.
The 'int' in int:pk denotes an integer and the pk denotes primary key. 
If you remember we created some books on our admin page and when saved it, that book automatically gets an id=1 by default, 
similary the id for the next books gets incremented by +1 
which means the second book gets an id of 2 (id=2) and for third book (id=3) and so on.

Also, the BookDetailView uses this int:pk or id to show the details of a particular book. 
Means, if id '1' is requested we will see details of first book,
when id=2 then we get details of second book and so on. The BookCheckout will
work after this detail page which shows which book is going to be purchased by user and the last two urls are working seperately.
"""