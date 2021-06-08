from django.shortcuts import render


def view_400(request, exception,):
    return render(request, 'error_pages/400.html', status=400)

def view_403(request, exception,):
    return render(request, 'error_pages/403.html', status=403)

def view_404(request, exception,):
    return render(request, 'error_pages/404.html', status=404)

def view_500(request):
    return render(request, 'error_pages/500.html', status=500)