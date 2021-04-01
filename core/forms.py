from django import forms


class ParticipantForm(forms.Form):
    Image_of_Project = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control inp", "placeholder": ""}
        )
    )
