from django.contrib import admin
from .models import EventPlan, OptimalSolution

@admin.register(EventPlan)
class EventPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_budget', 'objective', 'created_at')
    list_filter = ('objective', 'created_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'

@admin.register(OptimalSolution)
class OptimalSolutionAdmin(admin.ModelAdmin):
    list_display = ('event_plan', 'optimal_guests', 'optimal_entertainment_units', 'total_cost', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('event_plan__title',) 