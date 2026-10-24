from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Conversation
from .forms import ConversationMessageForm

@login_required
def NewChat(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard')  # Use your actual dashboard URL name
        
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        return redirect('detailchat', pk=conversations.first().id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(item.created_by)
            conversation.members.add(request.user)  # FIX: Add current user to members
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('detailchat', pk=conversation.id)  # FIX: Use conversation.id instead of item_pk
    else:
        form = ConversationMessageForm()
        
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'conversation/chat.html', context)
         
@login_required
def chatBox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id]).distinct()
    context = {
        'conversations': conversations
    }
    return render(request, 'conversation/chatbox.html', context)
    
@login_required
def DetailedChat(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members__in=[request.user.id])

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            return redirect('detailchat', pk=pk)
    else:
        form = ConversationMessageForm()

    context = {
        'conversation': conversation,
        'form': form,
        'title': 'Chat',
    }
    return render(request, 'conversation/detailchat.html', context)


@login_required
def delete_conversation(request, pk):
  conversation = get_object_or_404(Conversation, pk=pk, members=request.user)
  conversation.delete()
  return redirect('chatbox')