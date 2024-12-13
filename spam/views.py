from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Click, CodeSubmission, AttemptCounter
from django.contrib import messages
# Create your views here.



def submit_code(request):
    if request.method == 'POST':
        # Hent tælleren (eller opret én, hvis den ikke findes)
        counter = AttemptCounter.objects.first()
        if not counter:
            counter = AttemptCounter.objects.create()

        # Tæl op
        counter.attempts += 1
        counter.save()

        # # Tilføj besked, der vises på forsiden
        messages.error(request, "Koden var forkert.")

        # Omdiriger til forsiden
        return redirect('index')  # 'index' er navnet på forsiden i `urls.py`

    # Hvis metoden ikke er POST, omdiriger til forsiden
    return redirect('index')

def index(request):
     # Hent brugerens IP og session
    ip = request.META.get('REMOTE_ADDR')
    session_key = request.session.session_key

    if not session_key:
        # Opret session, hvis den ikke findes
        request.session.create()

    # Tjek, om brugeren allerede er tracket
    if not Click.objects.filter(session_key=request.session.session_key).exists():
        # Opret en ny trackingpost
        Click.objects.create(
            ip_address=ip,
            session_key=request.session.session_key,
            user_agent=request.META.get('HTTP_USER_AGENT', 'unknown')
        )

    return render(request, 'spam/index.html')


def track_click(request):
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    Click.objects.create(ip_address=ip, user_agent=user_agent)
    return JsonResponse({'message': 'Click tracked!'})

def view_submissions(request):
    submissions = CodeSubmission.objects.all()
    return render(request, 'spam/submissions.html', {'submissions': submissions})

def view_visits(request):
    clicks = Click.objects.all()
    return render(request, 'spam/visits.html', {'clicks': clicks})


def login_view(request):
    return render(request, 'app/login.html')