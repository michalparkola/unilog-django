from django.shortcuts import render_to_response, get_object_or_404
from unilog_core.models import Tag, LogEntry

#def index(request):
#    entries = LogEntry.objects.all().order_by('-date')
#    return render_to_response('unilog_core/index.html', {'entries': entries})

#def detail(request, entry_id):
#    entry = get_object_or_404(LogEntry, pk=entry_id)
#    return render_to_response("unilog_core/details.html", {'entry':entry})