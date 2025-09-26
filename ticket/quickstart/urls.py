from django.urls import path
from .views import RecipeAPIView, TicketAPIView, SingleTicketApiView, SectorAPIView, TicketUpdateAPIView

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(),name='Receitas'),
    path('tickets/', TicketAPIView.as_view(),name='Chamados'),
    path('tickets/update/<int:pk>', TicketUpdateAPIView.as_view(), name='Atualizar chamado'),
    path('tickets/closed', TicketAPIView.as_view(), name='Chamados fechados'),
    path('tickets/<int:pk>',SingleTicketApiView.as_view(),name="Chamado"),
    path('sector/', SectorAPIView.as_view(), name="Setor")
]