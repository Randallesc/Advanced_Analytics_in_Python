"""
Fire Station Location Problem using Second-Order Conic Programming (SOCP)

Problem: Find the optimal location for a fire station to minimize the 
maximum distance to any village (minimax problem).
"""

import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

print("="*70)
print("FIRE STATION LOCATION PROBLEM - SOCP FORMULATION")
print("="*70)

# Set random seed for reproducibility
np.random.seed(42)

# Number of villages
n = 20

# Generate random village coordinates uniformly on [0, 10] × [0, 10]
print(f"\n{n} randomly generated village locations...")
villages = np.random.uniform(0, 10, size=(n, 2))

print("\nVillage coordinates:")
print("-" * 50)
for i in range(n):
    print(f"Village {i+1:2d}: v_{i+1} = ({villages[i, 0]:.3f}, {villages[i, 1]:.3f})")

print("\n" + "="*70)
print("SOCP FORMULATION")
print("="*70)

print("""
Mathematical Model:
-------------------
We want to minimize the maximum distance from the fire station to any village.

Decision Variables:
  x, y: Coordinates of the fire station location
  t: Maximum distance from fire station to any village

Objective:
  minimize t

Constraints (for each village i = 1, ..., n):
  ||v - v_i||_2 ≤ t
  
  where v = (x, y) is the fire station location
  and v_i = (x_i, y_i) is the location of village i

In component form:
  √[(x - x_i)² + (y - y_i)²] ≤ t  for all i

This is a Second-Order Cone constraint!
Each constraint has the form: ||(x - x_i, y - y_i)||_2 ≤ t
""")

print("\n" + "="*70)
print("SOLVING THE SOCP USING CVXPY")
print("="*70)

# Define decision variables
x = cp.Variable(name='x')
y = cp.Variable(name='y')
t = cp.Variable(name='t')

# Objective: minimize the maximum distance
objective = cp.Minimize(t)

# Constraints: For each village, distance from fire station ≤ t
constraints = []
for i in range(n):
    # Second-order cone constraint: ||v - v_i||_2 <= t
    # In CVXPY: cp.norm(vector, 2) <= t
    distance_vector = cp.vstack([x - villages[i, 0], y - villages[i, 1]])
    constraints.append(cp.norm(distance_vector, 2) <= t)

print(f"\nNumber of variables: 3 (x, y, t)")
print(f"Number of SOC constraints: {n}")

# Create and solve the problem
problem = cp.Problem(objective, constraints)

print("\nSolving SOCP...")
problem.solve(solver=cp.CLARABEL, verbose=False)

# Check solution status
print(f"\nSolution status: {problem.status}")

if problem.status == 'optimal':
    print("\n" + "="*70)
    print("OPTIMAL SOLUTION")
    print("="*70)
    
    # Extract optimal values
    x_opt = x.value
    y_opt = y.value
    t_opt = t.value
    
    print(f"\nOptimal fire station location:")
    print(f"  x* = {x_opt:.6f}")
    print(f"  y* = {y_opt:.6f}")
    print(f"  v* = ({x_opt:.6f}, {y_opt:.6f})")
    
    print(f"\nMinimum longest distance:")
    print(f"  t* = {t_opt:.6f}")
    
    # Verify the solution by computing actual distances
    print("\n" + "="*70)
    print("VERIFICATION: Distance from fire station to each village")
    print("="*70)
    
    distances = []
    for i in range(n):
        dist = np.sqrt((x_opt - villages[i, 0])**2 + (y_opt - villages[i, 1])**2)
        distances.append(dist)
        status = "MAX" if abs(dist - t_opt) < 1e-4 else ""
        print(f"Village {i+1:2d}: {dist:.6f} {status}")
    
    max_distance = max(distances)
    print(f"\nMaximum distance (verification): {max_distance:.6f}")
    print(f"Optimal objective value t*: {t_opt:.6f}")
    print(f"Difference: {abs(max_distance - t_opt):.2e}")
    
    # Count villages at maximum distance (on the boundary)
    villages_at_max = sum(1 for d in distances if abs(d - t_opt) < 1e-4)
    print(f"\nNumber of villages at maximum distance: {villages_at_max}")
    
    print("\n" + "="*70)
    print("VISUALIZATION")
    print("="*70)
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Plot villages
    ax.scatter(villages[:, 0], villages[:, 1], c='blue', s=100, marker='s', 
              label='Villages', zorder=3, edgecolors='darkblue', linewidths=2)
    
    # Label villages
    for i in range(n):
        ax.annotate(f'V{i+1}', (villages[i, 0], villages[i, 1]), 
                   xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    # Plot fire station
    ax.scatter(x_opt, y_opt, c='red', s=300, marker='*', 
              label='Fire Station', zorder=5, edgecolors='darkred', linewidths=2)
    ax.annotate('Fire Station', (x_opt, y_opt), 
               xytext=(10, 10), textcoords='offset points', 
               fontsize=12, fontweight='bold', color='red')
    
    # Draw circle with radius = maximum distance
    circle = plt.Circle((x_opt, y_opt), t_opt, color='red', fill=False, 
                       linestyle='--', linewidth=2, label=f'Coverage (r={t_opt:.3f})')
    ax.add_patch(circle)
    
    # Draw lines to villages at maximum distance
    for i in range(n):
        if abs(distances[i] - t_opt) < 1e-4:
            ax.plot([x_opt, villages[i, 0]], [y_opt, villages[i, 1]], 
                   'r-', linewidth=1.5, alpha=0.6, zorder=2)
    
    # Draw lines to all villages (lighter)
    for i in range(n):
        ax.plot([x_opt, villages[i, 0]], [y_opt, villages[i, 1]], 
               'gray', linewidth=0.5, alpha=0.3, zorder=1)
    
    ax.set_xlabel('x-coordinate', fontsize=12, fontweight='bold')
    ax.set_ylabel('y-coordinate', fontsize=12, fontweight='bold')
    ax.set_title('Optimal Fire Station Location (SOCP Solution)\n' + 
                f'Minimizing Maximum Distance: t* = {t_opt:.3f}', 
                fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/fire_station_location.png', dpi=300, bbox_inches='tight')
    print("\n✓ Saved visualization to: fire_station_location.png")
    
    # Create a zoomed-in view around the fire station
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    
    # Plot villages
    ax2.scatter(villages[:, 0], villages[:, 1], c='blue', s=150, marker='s', 
               label='Villages', zorder=3, edgecolors='darkblue', linewidths=2)
    
    # Label villages
    for i in range(n):
        ax2.annotate(f'{i+1}', (villages[i, 0], villages[i, 1]), 
                    fontsize=10, ha='center', va='center', color='white', fontweight='bold')
    
    # Plot fire station
    ax2.scatter(x_opt, y_opt, c='red', s=400, marker='*', 
               label='Fire Station', zorder=5, edgecolors='darkred', linewidths=3)
    
    # Draw circle
    circle2 = plt.Circle((x_opt, y_opt), t_opt, color='red', fill=False, 
                        linestyle='--', linewidth=3, label=f'Max Distance = {t_opt:.3f}')
    ax2.add_patch(circle2)
    
    # Highlight villages at maximum distance
    for i in range(n):
        if abs(distances[i] - t_opt) < 1e-4:
            ax2.plot([x_opt, villages[i, 0]], [y_opt, villages[i, 1]], 
                    'r-', linewidth=3, alpha=0.8, zorder=2, label='_nolegend_')
            # Draw a special marker
            ax2.scatter(villages[i, 0], villages[i, 1], c='yellow', s=300, 
                       marker='o', zorder=4, edgecolors='red', linewidths=3, alpha=0.5)
    
    ax2.set_xlabel('x-coordinate', fontsize=14, fontweight='bold')
    ax2.set_ylabel('y-coordinate', fontsize=14, fontweight='bold')
    ax2.set_title(f'Fire Station Coverage\n{villages_at_max} villages at maximum distance', 
                 fontsize=16, fontweight='bold')
    ax2.legend(fontsize=12, loc='best')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/fire_station_coverage.png', dpi=300, bbox_inches='tight')
    print("✓ Saved coverage visualization to: fire_station_coverage.png")
    
    # Statistics
    
    print(f"\nDistance statistics:")
    print(f"  Minimum distance to a village: {min(distances):.6f}")
    print(f"  Maximum distance to a village: {max(distances):.6f}")
    print(f"  Average distance to villages: {np.mean(distances):.6f}")
    print(f"  Median distance to villages: {np.median(distances):.6f}")
    print(f"  Standard deviation: {np.std(distances):.6f}")
    
    print(f"\nFire station location statistics:")
    print(f"  Distance from origin: {np.sqrt(x_opt**2 + y_opt**2):.6f}")
    print(f"  Within [0,10] × [0,10]? {0 <= x_opt <= 10 and 0 <= y_opt <= 10}")
    
else:
    print("\n✗ Problem could not be solved optimally!")
    print(f"Status: {problem.status}")

