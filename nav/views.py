from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from nav.models import Category, App


def index(request):
    respond_data = {'categories': Category.objects.all().order_by('-weight', )}
    return render(request, 'index.html', respond_data)


class AppDetailView(DetailView):
    model = App

    def app_detail_view(request, pk):
        try:
            app_id = App.objects.get(pk=pk)
        except App.DoesNotExist:
            raise Http404("App does not exist")

        return render(
            request,
            'nav/app_detail.html',
            context={'app': app_id, 'categories': Category.objects.all().order_by('-weight', )},
        )


def app_detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    categories = Category.objects.all().order_by('-weight', )
    return render(request, "nav/app_detail.html", {"app": app, "categories": categories})