from .models import User

def user_list(request):
    latest_users = User.object.order_by('-date_joined')[:6]
    return {'user_list': latest_users}
