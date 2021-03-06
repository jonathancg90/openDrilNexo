from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from apps.mail.models.Campaign import Campaign


class CampaignCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        super(CampaignCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        exclude = ['status']
        model = Campaign