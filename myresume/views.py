from django.http import FileResponse, Http404

# FileResponse's path starts at the project level.
def myresume(request):
    try:
        return FileResponse(open('myresume/resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
