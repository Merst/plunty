from django.views import generic
from .models import Attempt

class AttemptListView(generic.ListView):
    model = Attempt
    context_object_name = 'attempt_list'
    queryset = Attempt.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

# Adds a success count variable to templates
        context['success'] = len(Attempt.objects.filter(success=True))
        context['progress_rate'] = int(context['success']) / 20
    
        return context