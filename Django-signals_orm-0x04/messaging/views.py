from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

User = get_user_model()

@login_required
@require_POST
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('home')

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
