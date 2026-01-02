"""
Convex Cone Ordering Problem
Comparing vectors using different cone orderings
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("="*70)
print("CONVEX CONE ORDERING PROBLEM")
print("="*70)

# Define the vectors
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

print("\nGiven vectors:")
print(f"x = {x}")
print(f"y = {y}")

# Compute x - y
diff = x - y
print(f"\nx - y = {diff}")

print("\n" + "="*70)
print("PART (a): Non-negative Orthant ℝ³₊")
print("="*70)

print("\nRecall: x ≽_K y if and only if x - y ∈ K")
print("\nFor the non-negative orthant ℝ³₊:")
print("ℝ³₊ = {(x₁, x₂, x₃) : x₁ ≥ 0, x₂ ≥ 0, x₃ ≥ 0}")

print(f"\nChecking if x - y = {diff} ∈ ℝ³₊:")
print(f"  Component 1: {diff[0]} ≥ 0? {diff[0] >= 0} {'✓' if diff[0] >= 0 else '✗'}")
print(f"  Component 2: {diff[1]} ≥ 0? {diff[1] >= 0} {'✓' if diff[1] >= 0 else '✗'}")
print(f"  Component 3: {diff[2]} ≥ 0? {diff[2] >= 0} {'✓' if diff[2] >= 0 else '✗'}")

in_nonneg_orthant = np.all(diff >= 0)
print(f"\nIs x - y ∈ ℝ³₊? {in_nonneg_orthant}")
print(f"\nConclusion: x {'≽' if in_nonneg_orthant else '⊀'}_ℝ³₊ y")

if not in_nonneg_orthant:
    print("\nExplanation: Since the first component of x - y is negative (-2 < 0),")
    print("x - y is NOT in the non-negative orthant. Therefore, x is NOT greater")
    print("than or equal to y with respect to the ℝ³₊ ordering.")

# Plotting for part (a)
fig = plt.figure(figsize=(14, 6))

# Plot 1: x - y and the non-negative orthant
ax1 = fig.add_subplot(121, projection='3d')

# Draw the non-negative orthant (first octant)
# Create grid for the faces
grid_size = 3
u = np.linspace(0, grid_size, 10)
v = np.linspace(0, grid_size, 10)
U, V = np.meshgrid(u, v)

# xy-plane face (z=0)
ax1.plot_surface(U, V, np.zeros_like(U), alpha=0.2, color='blue')
# xz-plane face (y=0)
ax1.plot_surface(U, np.zeros_like(U), V, alpha=0.2, color='blue')
# yz-plane face (x=0)
ax1.plot_surface(np.zeros_like(U), U, V, alpha=0.2, color='blue')

# Plot x - y
ax1.scatter(*diff, color='red', s=100, marker='o', label=f'x - y = {diff}')
ax1.quiver(0, 0, 0, diff[0], diff[1], diff[2], color='red', arrow_length_ratio=0.1, linewidth=2)

# Plot axes
ax1.plot([0, grid_size], [0, 0], [0, 0], 'k-', linewidth=1)
ax1.plot([0, 0], [0, grid_size], [0, 0], 'k-', linewidth=1)
ax1.plot([0, 0], [0, 0], [0, grid_size], 'k-', linewidth=1)

ax1.set_xlabel('x₁', fontsize=12)
ax1.set_ylabel('x₂', fontsize=12)
ax1.set_zlabel('x₃', fontsize=12)
ax1.set_title('Part (a): x - y and ℝ³₊ (Non-negative Orthant)', fontsize=12, fontweight='bold')
ax1.legend()
ax1.set_xlim([-3, 3])
ax1.set_ylim([-1, 3])
ax1.set_zlim([-1, 3])

print("\n" + "="*70)
print("PART (b): Second-Order Cone L³")
print("="*70)

print("\nFor the second-order cone (Lorentz cone) L³:")
print("L³ = {(t, x₁, x₂) : t ≥ √(x₁² + x₂²)}")
print("\nFor x - y = [{}, {}, {}]:".format(diff[0], diff[1], diff[2]))
print(f"  t = {diff[0]}")
print(f"  x₁ = {diff[1]}")
print(f"  x₂ = {diff[2]}")

norm_tail = np.sqrt(diff[1]**2 + diff[2]**2)
print(f"\nChecking if t ≥ √(x₁² + x₂²):")
print(f"  {diff[0]} ≥ √({diff[1]}² + {diff[2]}²)")
print(f"  {diff[0]} ≥ √{diff[1]**2 + diff[2]**2}")
print(f"  {diff[0]} ≥ {norm_tail:.4f}")

in_soc = diff[0] >= norm_tail
print(f"\nIs the condition satisfied? {in_soc} {'✓' if in_soc else '✗'}")
print(f"\nIs x - y ∈ L³? {in_soc}")
print(f"\nConclusion: x {'≽' if in_soc else '⊀'}_L³ y")

if not in_soc:
    print(f"\nExplanation: We need t ≥ √(x₁² + x₂²), i.e., {diff[0]} ≥ {norm_tail:.4f}")
    print(f"Since {diff[0]} < {norm_tail:.4f}, the point x - y is OUTSIDE the second-order cone.")
    print("Therefore, x is NOT greater than or equal to y with respect to L³.")

# Plot 2: x - y and the second-order cone
ax2 = fig.add_subplot(122, projection='3d')

# Create the second-order cone
theta = np.linspace(0, 2*np.pi, 50)
t_vals = np.linspace(0, 3, 50)
THETA, T = np.meshgrid(theta, t_vals)

# For second-order cone: t >= sqrt(x1^2 + x2^2)
# Parametrize as: x1 = r*cos(theta), x2 = r*sin(theta), t = r (on boundary)
X1 = T * np.cos(THETA)
X2 = T * np.sin(THETA)
T_surface = T  # On the boundary: t = sqrt(x1^2 + x2^2)

ax2.plot_surface(T_surface, X1, X2, alpha=0.3, color='green', label='L³')

# Plot x - y
ax2.scatter(diff[0], diff[1], diff[2], color='red', s=100, marker='o', 
           label=f'x - y = [{diff[0]}, {diff[1]}, {diff[2]}]')
ax2.quiver(0, 0, 0, diff[0], diff[1], diff[2], color='red', arrow_length_ratio=0.1, linewidth=2)

# Plot axes
ax2.plot([0, 3], [0, 0], [0, 0], 'k-', linewidth=1)
ax2.plot([0, 0], [-3, 3], [0, 0], 'k-', linewidth=1)
ax2.plot([0, 0], [0, 0], [-3, 3], 'k-', linewidth=1)

ax2.set_xlabel('t (x₀)', fontsize=12)
ax2.set_ylabel('x₁', fontsize=12)
ax2.set_zlabel('x₂', fontsize=12)
ax2.set_title('Part (b): x - y and L³ (Second-Order Cone)', fontsize=12, fontweight='bold')
ax2.legend()
ax2.set_xlim([-3, 3])
ax2.set_ylim([-3, 3])
ax2.set_zlim([-1, 3])

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/cone_ordering_visualization.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved visualization to: cone_ordering_visualization.png")

print("\n" + "="*70)
print("PART (c): Positive Semidefinite Cone S³₊")
print("="*70)

# Define the matrices
A = np.array([[-6,   7,   8],
              [ 7,  -8,   9],
              [ 8,   9, -10]])

B = np.array([[0, 1, 2],
              [1, 2, 3],
              [2, 3, 4]])

C = np.array([[-10,  9,   8],
              [  9, -8,   7],
              [  8,  7, -12]])

print("\nGiven matrices:")
print("\nA =")
print(A)
print("\nB =")
print(B)
print("\nC =")
print(C)

print("\nRecall: For matrices, A ≽_S³₊ B if and only if A - B ⪰ 0")
print("(i.e., A - B is positive semidefinite)")
print("\nA matrix is positive semidefinite if all its eigenvalues are ≥ 0.")

# Check A ≽ B
print("\n" + "-"*70)
print("Checking: Is A ≽_S³₊ B?")
print("-"*70)

A_minus_B = A - B
print("\nA - B =")
print(A_minus_B)

# Check if symmetric
is_symmetric_AB = np.allclose(A_minus_B, A_minus_B.T)
print(f"\nIs A - B symmetric? {is_symmetric_AB}")

if is_symmetric_AB:
    eigenvalues_AB = np.linalg.eigvalsh(A_minus_B)
    print(f"\nEigenvalues of A - B: {eigenvalues_AB}")
    
    all_nonneg_AB = np.all(eigenvalues_AB >= -1e-10)  # Small tolerance for numerical errors
    
    print(f"\nAre all eigenvalues ≥ 0? {all_nonneg_AB}")
    
    if all_nonneg_AB:
        print("\n✓ A - B is positive semidefinite")
        print("✓ Therefore: A ≽_S³₊ B is TRUE")
    else:
        print("\n✗ A - B has negative eigenvalues")
        print("✗ Therefore: A ≽_S³₊ B is FALSE")
        print(f"\nSmallest eigenvalue: {eigenvalues_AB.min():.6f}")
else:
    print("\n✗ A - B is not symmetric, so it cannot be in S³₊")
    print("✗ Therefore: A ≽_S³₊ B is FALSE")

# Check A ≽ C
print("\n" + "-"*70)
print("Checking: Is A ≽_S³₊ C?")
print("-"*70)

A_minus_C = A - C
print("\nA - C =")
print(A_minus_C)

# Check if symmetric
is_symmetric_AC = np.allclose(A_minus_C, A_minus_C.T)
print(f"\nIs A - C symmetric? {is_symmetric_AC}")

if is_symmetric_AC:
    eigenvalues_AC = np.linalg.eigvalsh(A_minus_C)
    print(f"\nEigenvalues of A - C: {eigenvalues_AC}")
    
    all_nonneg_AC = np.all(eigenvalues_AC >= -1e-10)
    
    print(f"\nAre all eigenvalues ≥ 0? {all_nonneg_AC}")
    
    if all_nonneg_AC:
        print("\n✓ A - C is positive semidefinite")
        print("✓ Therefore: A ≽_S³₊ C is TRUE")
    else:
        print("\n✗ A - C has negative eigenvalues")
        print("✗ Therefore: A ≽_S³₊ C is FALSE")
        print(f"\nSmallest eigenvalue: {eigenvalues_AC.min():.6f}")
else:
    print("\n✗ A - C is not symmetric, so it cannot be in S³₊")
    print("✗ Therefore: A ≽_S³₊ C is FALSE")

print("\n" + "="*70)
print("SUMMARY OF RESULTS")
print("="*70)

print("\n(a) Using ℝ³₊: x ⊀_ℝ³₊ y")
print("    Reason: x - y = [-2, 0, 2] has a negative component")

print("\n(b) Using L³: x ⊀_L³ y")
print(f"    Reason: For x - y = [{diff[0]}, {diff[1]}, {diff[2]}], we need")
print(f"    {diff[0]} ≥ {norm_tail:.4f}, which is false")

print("\n(c) Using S³₊:")
if 'all_nonneg_AB' in locals() and all_nonneg_AB:
    print("    A ≽_S³₊ B is TRUE")
else:
    print("    A ≽_S³₊ B is FALSE")
    
if 'all_nonneg_AC' in locals() and all_nonneg_AC:
    print("    A ≽_S³₊ C is TRUE")
else:
    print("    A ≽_S³₊ C is FALSE")

print("\n" + "="*70)
print("DONE!")
print("="*70)