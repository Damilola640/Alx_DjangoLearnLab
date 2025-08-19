from rest_framework import generics, permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter


# ------------------------
# LIST + CREATE
# ------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books (public, with filters).
    POST: Create a new book (authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter

    search_fields = ['title']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['publication_year']  # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [permissions.AllowAny()]


# ------------------------
# RETRIEVE + UPDATE + DELETE
# ------------------------
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book by ID (public).
    PUT/PATCH/DELETE: Authenticated only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [permissions.AllowAny()]


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
    """
    GET: List all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filter backends and ordering fields
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title'] # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]