from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.http import JsonResponse

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session['user_id'] = user.id
            request.session['is_logged_in'] = True
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    request.session.flush()
    logout(request)
    return redirect('login')

@login_required
def manage_sessions(request):
    sessions = Session.objects.filter(expire_date__gte=now())
    session_data = []

    for session in sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id')
        username = None

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                username = user.username
            except User.DoesNotExist:
                username = "Unknown User"

        session_data.append({
            'session_key': session.session_key,
            'user_id': user_id,
            'username': username,
            'expire_date': session.expire_date,
        })

    return render(request, 'manage_sessions.html', {'sessions': session_data})


def update_session_activity(request):
    if request.user.is_authenticated:
        session_key = request.session.session_key
        if session_key:
            last_activity_time = request.session.get('last_activity_time', now())

            if isinstance(last_activity_time, str):
                last_activity_time = datetime.fromisoformat(last_activity_time)

            inactivity_threshold = 1 * 60
            time_diff = (now() - last_activity_time).total_seconds()

            if time_diff > inactivity_threshold:
                request.session['status'] = 'pending'
            else:
                request.session['status'] = 'active'

            request.session['last_activity_time'] = now().isoformat()

    return JsonResponse({'status': request.session.get('status', 'inactive')})

@login_required
def dashboard(request):
    update_session_activity(request)

    username = request.session.get('username')
    user_id = request.session.get('user_id')
    is_logged_in = request.session.get('is_logged_in', False)
    session_key = request.session.session_key
    user_status = request.session.get('status', 'inactive')
    last_activity_time = request.session.get('last_activity_time')

    return render(request, 'dashboard.html', {
        'username': username,
        'user_id': user_id,
        'is_logged_in': is_logged_in,
        'session_key': session_key,
        'user_status': user_status,
        'last_activity_time': last_activity_time,
    })