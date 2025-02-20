from django import forms
from django.core.exceptions import ValidationError


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
