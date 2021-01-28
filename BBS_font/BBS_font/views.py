from django.shortcuts import render


def search_view(request):
    if request.method == 'GET':
        return render(request, 'search_result.html')