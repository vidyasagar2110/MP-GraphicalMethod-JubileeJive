import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def solve_graphical_method(event_plan):
    """
    Solve the linear programming problem using the graphical method.
    Returns the optimal solution and a base64 encoded plot.
    """
    # Extract parameters
    budget = float(event_plan.total_budget)
    cost_guest = float(event_plan.cost_per_guest)
    cost_ent = float(event_plan.cost_per_entertainment)
    min_guests = event_plan.min_guests
    min_ent = event_plan.min_entertainment_units

    # Calculate maximum possible values based on budget
    max_possible_guests = int(budget / cost_guest)
    max_possible_ent = int(budget / cost_ent)

    # Create points for plotting with some padding for better visualization
    x = np.linspace(0, max_possible_guests * 1.2, 1000)
    
    # Budget constraint line: cost_guest * x + cost_ent * y = budget
    # Solve for y: y = (budget - cost_guest * x) / cost_ent
    y_budget = (budget - cost_guest * x) / cost_ent
    
    # Create the plot with a larger figure size and improved style
    plt.style.use('bmh')  # Using built-in style instead of seaborn
    plt.figure(figsize=(12, 9), facecolor='white')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Plot constraints with improved styling
    plt.plot(x, y_budget, label='Budget Constraint', color='#007bff', linewidth=2)
    plt.axvline(x=min_guests, color='#fd7e14', linestyle='--', 
                label='Min Guests Required', linewidth=2)
    plt.axhline(y=min_ent, color='#ffc107', linestyle='--', 
                label='Min Entertainment Required', linewidth=2)
    
    # Fill feasible region with improved styling
    y_feasible = y_budget.copy()
    y_feasible = np.maximum(y_feasible, min_ent)
    y_feasible = np.where(y_feasible < 0, 0, y_feasible)
    plt.fill_between(x, min_ent, y_feasible, 
                     where=(x >= min_guests), 
                     alpha=0.2, color='#6c757d',
                     label='Feasible Region')
    
    # Find corner points of feasible region
    corners = []
    
    # Point at minimum guests and minimum entertainment
    corners.append((min_guests, min_ent))
    
    # Intersection of budget line with min entertainment line
    x_at_min_ent = (budget - cost_ent * min_ent) / cost_guest
    if x_at_min_ent >= min_guests:
        corners.append((x_at_min_ent, min_ent))
    
    # Intersection of budget line with min guests line
    y_at_min_guests = (budget - cost_guest * min_guests) / cost_ent
    if y_at_min_guests >= min_ent:
        corners.append((min_guests, y_at_min_guests))
    
    # Find optimal solution based on objective
    if corners:  # Only proceed if there are feasible points
        if event_plan.objective == 'MAX_GUESTS':
            optimal_point = max(corners, key=lambda p: p[0])
        elif event_plan.objective == 'MAX_ENTERTAINMENT':
            optimal_point = max(corners, key=lambda p: p[1])
        else:  # BALANCED
            # Normalize and weight both objectives equally
            normalized_points = [
                (x/max_possible_guests + y/max_possible_ent, (x, y)) 
                for x, y in corners
            ]
            optimal_point = max(normalized_points, key=lambda p: p[0])[1]
        
        # Plot optimal point with improved styling
        plt.plot(optimal_point[0], optimal_point[1], 'ro', markersize=12, 
                label='Optimal Solution', color='#dc3545')
        
        # Add annotation for optimal point
        plt.annotate(f'({int(optimal_point[0])}, {int(optimal_point[1])})',
                    xy=optimal_point,
                    xytext=(10, 10),
                    textcoords='offset points',
                    ha='left',
                    va='bottom',
                    bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    else:
        return None
    
    # Customize plot
    plt.xlabel('Number of Guests', fontsize=12)
    plt.ylabel('Entertainment Units', fontsize=12)
    plt.title('Event Planning Optimization', fontsize=14, pad=20)
    
    # Improve legend positioning and style
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', 
              borderaxespad=0., frameon=True, fancybox=True, shadow=True)
    
    # Set axis limits with padding
    plt.xlim(0, max(max_possible_guests * 1.1, min_guests * 1.2))
    plt.ylim(0, max(max_possible_ent * 1.1, min_ent * 1.2))
    
    # Convert plot to base64 string with improved quality
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=300, 
                facecolor='white', edgecolor='none')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()
    
    graph = base64.b64encode(image_png).decode('utf-8')
    
    # Calculate total cost at optimal point
    total_cost = cost_guest * optimal_point[0] + cost_ent * optimal_point[1]
    
    return {
        'optimal_guests': int(optimal_point[0]),
        'optimal_entertainment_units': int(optimal_point[1]),
        'total_cost': total_cost,
        'graph': graph
    } 