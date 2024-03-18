from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from colorama import init, Fore
import time

from bezier_curve import bezier_divide_and_conquer_animate
from util import valid_int_input

# User input with color
init(autoreset=True)
print(Fore.LIGHTYELLOW_EX + "\nBézier Curve Generator\n")
n = valid_int_input(Fore.WHITE + "Number of control points (>=1): ", has_limit=True, lower_limit=1)
control_points = []
for i in range(n):
    print(Fore.LIGHTMAGENTA_EX + f"\n== Control Point {i + 1} ==")
    x = valid_int_input(Fore.WHITE + f"x{i + 1}: ")
    y = valid_int_input(Fore.WHITE + f"y{i + 1}: ")
    control_points.append((x, y))
iterations = valid_int_input(Fore.WHITE + "\nNumber of iterations (>=1): ", has_limit=True, lower_limit=1)

start = time.time()
curve_points, midpoints = bezier_divide_and_conquer_animate(control_points=control_points, iterations=iterations)
end = (time.time() - start) * 1000  # milliseconds

def update(frame):
    ax.clear()
    
    iteration = 0
    total_levels = 0
    while total_levels + len(midpoints[iteration]) <= frame:
        total_levels += len(midpoints[iteration])
        iteration += 1
    level = frame - total_levels

    # Plot control points
    control_x, control_y = zip(*control_points)
    ax.scatter(control_x, control_y, color='red', label='Control Points')
    ax.plot(control_x, control_y, color='red', linestyle='dashed', alpha=0.5)

    # Plot midpoints
    for iter_index in range(iteration + 1):
        for level_index in range(len(midpoints[iter_index])):
            if iter_index == iteration and level_index > level:
                break
            mid_x, mid_y = zip(*midpoints[iter_index][level_index])
            ax.plot(mid_x, mid_y, color='green', linestyle='dotted', alpha=0.5)

    # Plot final curve
    if frame == total_frames - 1:
        x, y = zip(*curve_points)
        ax.plot(x, y, color='black', label='Bézier Curve')
        ax.legend()

    ax.set_title(f"Bézier Curve (Divide and Conquer)\nProcess Time: {end:.2f} ms\nAnimating > 4 iterations may take times.")

fig, ax = plt.subplots()
total_frames = sum(len(levels) for levels in midpoints)
ani = FuncAnimation(fig, update, frames=range(total_frames), interval=10, repeat=False)
plt.show()