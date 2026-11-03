from django import forms

from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ["rating", "message"]
        widgets = {
            "rating": forms.NumberInput(
                attrs={
                    "min": 1,
                    "max": 5,
                }
            ),
            "message": forms.Textarea(
                attrs={"rows": 5}
            ),
        }

    def clean_rating(self):
        rating = self.cleaned_data["rating"]

        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                "Please choose a rating between 1 and 5."
            )

        return rating
    