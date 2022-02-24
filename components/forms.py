from django import forms
from tinymce.widgets import TinyMCE
from .models import Note


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class NoteAdminForm(forms.ModelForm):
    description : forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required':False, 'cols':30, 'rows':10}
        )
    )
    
    class Meta:
        model = Note
        fields = "__all__"