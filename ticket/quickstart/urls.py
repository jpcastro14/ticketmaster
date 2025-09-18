from django.urls import path
from .views import RecipeAPIView, TicketApiView

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(),name='Receitas'),
    path('tickets/', TicketApiView.as_view(),name='Chamados')
]