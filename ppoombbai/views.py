# Create your views here.
from django.views.generic import TemplateView


class SeasonListView(TemplateView):
    template_name = "ppoombbai/season_list.html"