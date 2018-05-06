from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    # str=''
    # for candidate in candidates:
    #     str += "{0} 기호{1}번({2}) <br>".format(candidate.name,candidate.party_number,candidate.area)
    #     str += candidate.introduction+" <p>"
    # return HttpResponse(str)
    context = {'candidates':candidates}
    return render(request, 'elections/index.html', context)
