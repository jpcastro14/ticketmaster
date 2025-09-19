from django.urls import path
from .views import RecipeAPIView, TicketApiView, SingleTicketApiView

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(),name='Receitas'),
    path('tickets/', TicketApiView.as_view(),name='Chamados'),
    path('tickets/<int:pk>',SingleTicketApiView.as_view(),name="Chamado")
]