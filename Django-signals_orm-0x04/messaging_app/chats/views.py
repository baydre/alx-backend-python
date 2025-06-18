from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60)
def conversation_messages(request, conversation_id):
    pass
