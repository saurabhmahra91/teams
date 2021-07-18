from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'whatsapp/index.html')

def room(request):
    username = request.GET.get('username')
    room = request.GET.get('room')
    context = {'room':room, 'username':username}
    return render(request, 'whatsapp/room.html', context)