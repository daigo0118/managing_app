from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("出勤,退勤")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "polls/index.html")