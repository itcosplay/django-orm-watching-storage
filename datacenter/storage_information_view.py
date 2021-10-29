from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []

    for visitor in Visit.objects.filter(leaved_at=None):
        data_visitor = {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': visitor.format_duration()
        }

        non_closed_visits.append(data_visitor)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
