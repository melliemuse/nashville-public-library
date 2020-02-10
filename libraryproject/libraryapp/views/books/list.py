import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            # sqlite3.Row - allows us to reference keys on tuples which are columns in dataset
            # end up with list of class instances 
            # conn.row_factory = sqlite3.Row
            # db_cursor = conn.cursor()

            # db_cursor.execute("""
            # select
            #     b.id,
            #     b.title,
            #     b.isbn,
            #     b.author,
            #     b.year_published,
            #     b.librarian_id,
            #     b.location_id
            # from libraryapp_book b
            # """)
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            
        template = 'books/list.html'
        # dictionary of values being passed into template
        context = {
            'all_books': all_books
        }
        # positional args passing into render method
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['author'],
                form_data['isbn'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))