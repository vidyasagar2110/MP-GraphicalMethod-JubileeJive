from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class EventPlan(models.Model):
    OBJECTIVE_CHOICES = [
        ('MAX_GUESTS', 'Maximize Number of Guests'),
        ('MAX_ENTERTAINMENT', 'Maximize Entertainment Quality'),
        ('BALANCED', 'Balance Both Objectives'),
    ]

    title = models.CharField(max_length=200)
    total_budget = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    cost_per_guest = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    cost_per_entertainment = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    min_guests = models.PositiveIntegerField(
        default=1,
        help_text="Minimum number of guests required"
    )
    min_entertainment_units = models.PositiveIntegerField(
        default=1,
        help_text="Minimum number of entertainment units required"
    )
    objective = models.CharField(
        max_length=20,
        choices=OBJECTIVE_CHOICES,
        default='BALANCED'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Check if minimum costs are affordable with the budget
        min_entertainment_cost = self.cost_per_entertainment * self.min_entertainment_units
        min_guest_cost = self.cost_per_guest * self.min_guests
        min_total_cost = min_entertainment_cost + min_guest_cost
        
        if min_total_cost > self.total_budget:
            raise ValidationError(
                'The minimum required cost (minimum guests + minimum entertainment) exceeds the total budget.'
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - Budget: ${self.total_budget}"

class OptimalSolution(models.Model):
    event_plan = models.OneToOneField(
        EventPlan,
        on_delete=models.CASCADE,
        related_name='optimal_solution'
    )
    optimal_guests = models.PositiveIntegerField()
    optimal_entertainment_units = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solution for {self.event_plan.title}" 