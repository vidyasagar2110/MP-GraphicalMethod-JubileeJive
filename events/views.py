from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import EventPlan, OptimalSolution
from .forms import EventPlanForm
from .utils import solve_graphical_method

def home(request):
    """Home page view."""
    return render(request, 'events/home.html')

def create_plan(request):
    """Create a new event plan."""
    if request.method == 'POST':
        form = EventPlanForm(request.POST)
        if form.is_valid():
            event_plan = form.save()
            solution = solve_graphical_method(event_plan)
            
            if solution:
                OptimalSolution.objects.create(
                    event_plan=event_plan,
                    optimal_guests=solution['optimal_guests'],
                    optimal_entertainment_units=solution['optimal_entertainment_units'],
                    total_cost=solution['total_cost']
                )
                return redirect('view_solution', pk=event_plan.pk)
            else:
                messages.error(request, 'No feasible solution exists for the given constraints.')
                return redirect('create_plan')
    else:
        form = EventPlanForm()
    
    return render(request, 'events/create_plan.html', {'form': form})

def view_solution(request, pk):
    """View the solution for an event plan."""
    event_plan = get_object_or_404(EventPlan, pk=pk)
    solution = solve_graphical_method(event_plan)
    
    context = {
        'event_plan': event_plan,
        'solution': solution,
        'graph': solution['graph']
    }
    return render(request, 'events/view_solution.html', context)

def plan_list(request):
    """List all event plans."""
    plans = EventPlan.objects.all().order_by('-created_at')
    return render(request, 'events/plan_list.html', {'plans': plans})

def delete_plan(request, pk):
    """Delete an event plan."""
    event_plan = get_object_or_404(EventPlan, pk=pk)
    if request.method == 'POST':
        event_plan.delete()
        messages.success(request, 'Event plan deleted successfully.')
        return redirect('plan_list')
    return redirect('plan_list')

def view_steps(request):
    return render(request, 'events/steps.html')

def view_applications(request):
    return render(request, 'events/applications.html') 