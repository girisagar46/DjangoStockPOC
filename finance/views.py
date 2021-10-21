from django.views.generic import TemplateView, ListView, DetailView
from django_filters.views import FilterView

from .filters import StockFilter
from .models import StockHistory


class LandingView(TemplateView):
    template_name = 'index.html'


class StockHistoryListHTMLView(FilterView, ListView):
    model = StockHistory
    template_name = "stockhistory_list.html"
    http_method_names = ('get', 'post',)
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(StockHistoryListHTMLView, self).get_context_data(**kwargs)
        context['filter'] = StockFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return StockHistory.objects.all()\
            .order_by("-date")\
            .values("pk", "company_symbol__symbol", "date", "open", "high", "low", "close", "change_percent")


class StockHistoryDetailHTMLView(DetailView):
    model = StockHistory
    template_name = "stock_detail.html"
