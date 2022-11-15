from .models import Note
import django_filters

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ['id']