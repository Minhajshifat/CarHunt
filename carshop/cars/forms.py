from django import forms
from .models import carModel, CommentModel


class carForm(forms.ModelForm):
    class Meta:
        model = carModel
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["name", "email", "body"]
