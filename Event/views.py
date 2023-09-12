from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from datetime import datetime
from django.views.generic import ListView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'day.html'
    context_object_name = 'events'
    ordering = ['-date']  

    def get_queryset(self):
        queryset = super().get_queryset()
        date_param = self.request.GET.get('date')
        if date_param:
            queryset = queryset.filter(date=date_param)
        return queryset

@login_required
def some_view(request):
    if request.method == 'POST':
        event = Event.objects.create(name='Some Event', description='Description here', date='2023-09-15')
        event.people = request.user
        event.save()
        return redirect('success_page')
    return render(request, 'articles.html')

class HomeView(TemplateView):
    template_name = "calendar.html"

    def common_logic(self, request):
        events = Event.objects.all()
        form = EventForm()
        context = {'events': events, 'form': form}
        return context

    def get(self, request):
        context = self.common_logic(request)
        return render(request, self.template_name, context)

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.people = request.user
            event.save()
            return redirect('articles')
        context = self.common_logic(request)
        context['form'] = form
        return render(request, self.template_name, context)

class ArtView(TemplateView):
    template_name = "articles.html"

    def get(self, request):
        events = Event.objects.all()
        context = {'events': events}
        return render(request, self.template_name, context)

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.people = request.user
            event.save()
            return redirect('articles')
        events = Event.objects.all()
        context = {'events': events, 'form': form}
        return render(request, self.template_name, context)
    

class ArticleDetailView(View):
    template_name = "article_detail.html"

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        context = {'event': event}
        return render(request, self.template_name, context)

class DayView(View):
    template_name = 'day.html'

    def get(self, request):
        selected_date = request.GET.get('date')
        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        except ValueError:
            selected_date = None
        events = Event.objects.filter(date=selected_date) if selected_date else []
        context = {
            'selected_date': selected_date,
            'events': events,
        }
        return render(request, self.template_name, context)




