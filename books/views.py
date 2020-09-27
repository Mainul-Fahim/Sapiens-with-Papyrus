from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



"""The 'BookListView' is a class which basically using the django module ListView
to output the contents of Our book model (as i choose model = Book) in a list manner and
the template on which its working on is list.html.
"""

class BooksListView(ListView):
    model = Book
    template_name = 'list.html'

"""Similarly, the class 'BookDetailView' class using DetailView to output the contents of Our book model
in a detailed manner and the template on which its working on is detail.html.
"""

class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'

"""The class 'SearchResultsView' class using ListView which provides the search results in a list manner
 and the template on which its working on is search_results.html. 
 The SearchResultsView will match the search input provided by the user
 with the book title and the author's name (means you can search a book by its name or by its author name)
"""


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)


"""The 'BookCheckoutView' is a class using DetailView and 
the template on which its working on is checkout.html. 
So that user can confirm that they are paying for the right book.
"""

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


"""At last, we have a function called paymentComplete which basically keeps a record of which book 
is being purchased by the user 
and 
that record gets updated in our Order Model. 
The payment process can be completed in two ways, by using paypal or debit card.
"""

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

