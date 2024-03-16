import time
import matplotlib.pyplot as plt
from bezier_curve import bezier_divide_and_conquer, bezier_bruteforce

# Test cases
tests = [
    ([(0, 0), (100, 200), (300, 300), (500, 0)], 20),
    ([(0, 0), (100, 200), (200, 0), (300, 200), (400, 0)], 20),
    ([(0, 0), (100, 100), (200, 200), (300, 300), (400, 400), (500, 500)], 15),
    ([(0, 0), (50, 150), (100, 0), (150, 150), (200, 0)], 15),
    ([(0, 0), (200, 400), (400, 0), (600, 400), (800, 0)], 15),
    ([(0, 0), (100, 300), (200, 100), (300, 300), (400, 100), (500, 300)], 20)
]

# Show graph toggle
show_graph = False

# Test
for test_num, (control_points, iterations) in enumerate(tests, start=1):
    print(f"\nTest {test_num}:")
    print(f"Number of Control Points: {len(control_points)}")
    print(f"Control Points: {control_points}")
    print(f"Midpoint DnC Iterations: {iterations}")

    num_points = 2 ** iterations + 1

    # Divide and Conquer
    start = time.time()
    curve_dnc = bezier_divide_and_conquer(control_points=control_points, iterations=iterations)
    end = time.time() - start
    print(f"Divide and Conquer time: {end * 1000:.2f}ms")

    # Bruteforce
    start = time.time()
    curve_bf = bezier_bruteforce(control_points=control_points, num_points=num_points)
    end = time.time() - start
    print(f"Bruteforce time: {end * 1000:.2f}ms")

    if show_graph:
        # Plot curve from Divide and Conquer
        x_dnc, y_dnc = zip(*curve_dnc)
        plt.plot(x_dnc, y_dnc, label='Bézier Curve (D&C)', color='blue')

        # Plot curve from Bruteforce
        x_bf, y_bf = zip(*curve_bf)
        plt.plot(x_bf, y_bf, label='Bézier Curve (Bruteforce)', color='green', linestyle='dotted')

        control_x, control_y = zip(*control_points)
        plt.scatter(control_x, control_y, color='red', label='Control Points')
        plt.plot(control_x, control_y, color='red', linestyle='dashed', alpha=0.5)

        plt.legend()
        plt.title(f"Test {test_num}")
        plt.show()