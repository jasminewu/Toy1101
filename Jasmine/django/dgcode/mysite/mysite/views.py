from django.shortcuts import render_to_response
import datetime
def current_datetime(request):
    current_date = datetime.datetime.now()
    # return render_to_response('test1.html',{'current_date': current_date})
    return render_to_response('test1.html', locals())
#
# def hour_ahead(request, offset):
#     offset = int(offset)
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)
