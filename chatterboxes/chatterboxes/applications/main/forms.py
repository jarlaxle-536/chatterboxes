import django.forms as forms

class ChatSettingsForm(forms.Form):
    allow_bots_field = forms.BooleanField(required=False)
