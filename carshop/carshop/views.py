from django.shortcuts import render
from cars.models import carModel
from carBrand.models import Brand
from cars.forms import CommentForm
from django.views.generic import DetailView
from cars.models import carModel


def home(request, catagories_slug=None):
    data = carModel.objects.all()
    total = carModel.objects.all().count()
    if catagories_slug is not None:
        brand = Brand.objects.get(slug=catagories_slug)
        data = carModel.objects.filter(brand_name=brand)
    brand = Brand.objects.all()
    return render(request, "home.html", {"data": data, "brands": brand, "total": total})


class DetailPostView(DetailView):
    model = carModel
    pk_url_kwarg = "id"
    template_name = "details.html"
    context_object_name = "car"

    def car(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object  # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
