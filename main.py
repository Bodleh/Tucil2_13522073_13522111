import matplotlib.pyplot as plt
from util import valid_int_input
from bezier_curve import bezier_divide_and_conquer

# User input
n = valid_int_input("Number of control points: ", True, 3)
control_points = []
for i in range(n):
    x = valid_int_input(f"x{i + 1}: ")
    y = valid_int_input(f"y{i + 1}: ")
    control_points.append((x, y))
iterations = valid_int_input("Number of iterations: ", True, 1)

# Process
bezier_curve = bezier_divide_and_conquer(control_points=control_points, iterations=iterations)
print(bezier_curve)

# Plot curve
x, y = zip(*bezier_curve)
plt.plot(x, y, label='Bézier Curve')

# Plot control points
control_x, control_y = zip(*control_points)
plt.scatter(control_x, control_y, color='red', label='Control Points')
plt.plot(control_x, control_y, color='red', linestyle='dashed', alpha=0.5)

plt.legend()
plt.show()