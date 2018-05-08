from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404

from .models import Candidate, Poll, Choice

import datetime
from django.db.models import Sum

# Create your views here.
def index(request):
    candidates=Candidate.objects.all()
    # str=''
    # for candidate in candidates:
    #     str += "{0} 기호{1}번({2}) <br>".format(candidate.name,candidate.party_number,candidate.area)
    #     str += candidate.introduction+" <p>"
    # return HttpResponse(str)
    context={'candidates':candidates}
    return render(request, 'elections/index.html', context)

def candidates(request, name):
    candidate = get_object_or_404(Candidate, name=name)
    # try:
    #     candidate=Candidate.objects.get(name=name)
    # except:
    #     # return HttpResponseNotFound("없는 페이지 입니다.")
    #     raise Http404
    return HttpResponse(candidate.name)

def areas(request, area):
    # return HttpResponse(area)
    today=datetime.datetime.now()
    poll=None
    candidats=None
    try:
        poll=Poll.objects.get(area=area)
        # poll=Poll.object.get(area=area, start_date__lte=today, end_date__gte=today)
        candidates=Candidate.objects.filter(area=area)
    except:
        poll=None
        candidates=None

    context={'candidates':candidates,
        'area':area,
        'poll':poll}
    return render(request, 'elections/area.html', context)

def polls(request, poll_id):
    poll=Poll.objects.get(pk=poll_id)
    selection=request.POST['choice']
    try:
        choice=Choice.objects.get(poll_id=poll_id, candidate_id=selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
        choice.save()
    return HttpResponseRedirect("/areas/{}/results".format(poll.area))

def results(request, area):
    candidates = Candidate.objects.filter(area=area)

    polls=Poll.objects.filter(area=area)
    poll_results=[]
    for poll in polls:
        result={}
        result['start_date']=poll.start_date
        result['end_date']=poll.end_date

        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']

        rates=[]
        print(poll)
        print(total_votes)
        print(candidates)
        for candidate in candidates:
            try:
                print(poll, candidate)
                choice=Choice.objects.get(poll=poll,
                    candidate=candidate)
                rates.append(
                    round(choice.votes*100/result['total_votes'], 1)
                )
            except:
                rates.append(0)

        result['rates']=rates
        poll_results.append(result)

    context={'candidates':candidates, 'area':area,
        'poll_results':poll_results}
    return render(request, 'elections/results.html', context)
