from django import forms
from .models import EventPlan

class EventPlanForm(forms.ModelForm):
    class Meta:
        model = EventPlan
        fields = [
            'title',
            'total_budget',
            'cost_per_guest',
            'cost_per_entertainment',
            'min_guests',
            'min_entertainment_units',
            'objective'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'total_budget': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'cost_per_guest': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'cost_per_entertainment': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'min_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'min_entertainment_units': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'objective': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Event Title',
            'total_budget': 'Total Budget ($)',
            'cost_per_guest': 'Cost per Guest ($)',
            'cost_per_entertainment': 'Cost per Entertainment Unit ($)',
            'min_guests': 'Minimum Number of Guests Required',
            'min_entertainment_units': 'Minimum Entertainment Units Required',
            'objective': 'Optimization Objective'
        }
        help_texts = {
            'min_guests': 'The minimum number of guests that must be accommodated',
            'min_entertainment_units': 'The minimum number of entertainment units required for the event',
        }

    def clean(self):
        cleaned_data = super().clean()
        total_budget = cleaned_data.get('total_budget')
        cost_per_guest = cleaned_data.get('cost_per_guest')
        cost_per_entertainment = cleaned_data.get('cost_per_entertainment')
        min_guests = cleaned_data.get('min_guests')
        min_entertainment_units = cleaned_data.get('min_entertainment_units')

        if all([total_budget, cost_per_guest, cost_per_entertainment, min_guests, min_entertainment_units]):
            min_cost = (cost_per_guest * min_guests) + (cost_per_entertainment * min_entertainment_units)
            if min_cost > total_budget:
                raise forms.ValidationError(
                    "The minimum required cost exceeds the total budget. Please adjust your parameters."
                )

        return cleaned_data 