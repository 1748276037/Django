from django.urls import path
from book.views import index,readbook,Qd,formdata,header,jsonresponse,To_index
urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/', readbook),
    path('qd/',Qd).
    path('formdata/',formdata),
    path('header/',header),
    path('jsonresponse/',jsonresponse),
    path('To_index/',To_index)
]