from django import forms

from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            "make",
            "model",
            "category",
            "daily_price",
            "seats",
            "transmission",
            "description",
            "image",
        ]

    def clean_daily_price(self):
        daily_price = self.cleaned_data["daily_price"]

        if daily_price <= 0:
            raise forms.ValidationError(
                "Daily price must be greater than zero."
            )

        return daily_price
    