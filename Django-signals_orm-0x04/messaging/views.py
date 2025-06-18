from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import Prefetch
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

@login_required
def threaded_conversation(request, message_id):
    root_message = Message.objects.select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    ).get(pk=message_id, parent_message__isnull=True)

    def get_replies(message):
        replies = message.replies.all()
        return [
            {
                'message': reply,
                'replies': get_replies(reply)
            }
            for reply in replies
        ]

    context = {
        'root_message': root_message,
        'thread': get_replies(root_message)
    }
    return render(request, 'messaging/threaded_conversation.html', context)

@login_required
def user_sent_messages(request):
    # Only messages sent by the logged-in user
    messages = Message.objects.filter(sender=request.user).select_related('receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    )
    return render(request, 'messaging/user_sent_messages.html', {'messages': messages})

@login_required
def unread_inbox(request):
    unread_messages = Message.unread.unread_for_user(request.user).only('id', 'sender', 'content', 'timestamp')
    return render(request, 'messaging/unread_inbox.html', {'unread_messages': unread_messages})
