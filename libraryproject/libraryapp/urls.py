from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', list_libraries, name='libraries'),
    path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form')
]