from django.urls import path
from . import views

urlpatterns = [
    path('send',views.SentLetterView.as_view()),
    path('recever',views.GetLetterView.as_view()),
    path("list",views.ListGetBottles.as_view()),
    path("listitem",views.ListItem.as_view()),
    path("listsend",views.ListSendBottles.as_view()),
    path('answer',views.Answer.as_view()),
    path("ranking",views.Ranking.as_view())
]
