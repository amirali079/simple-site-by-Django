from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from MoNarm.models import Data, Article


def Hi(request):
    return HttpResponse("GoodBye World! :/")


def renderer(request):
    contex = {
        "data": Data.objects.all(),

    }
    return render(request, "MoNarm/home.html", contex)


def detailData(request, slug):
    contex = {
        "data": Data.objects.get(slug=slug)
    }
    return render(request, "MoNarm/details.html", contex)


def Becha(request):
    data = {
        1:
            {"name": "Amirali",
             "last_name": "goli",
             "rank": 20
             },
        2:
            {"name": "Naser",
             "last_name": "FarajZade",
             "rank": 19
             },
        3:
            {"name": "Ali",
             "last_name": "Mahvash",
             "rank": 0
             }
    }
    return JsonResponse(data)
