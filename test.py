import time
import matplotlib.pyplot as plt
from bezier_curve import bezier_divide_and_conquer, bezier_bruteforce

# Test cases
tests = [
    ([(0, 0), (100, 200), (300, 300), (500, 0)], 15),
    ([(0, 0), (100, 200), (200, 0), (300, 200), (400, 0)], 15),
    ([(0, 0), (100, 300), (200, -100), (300, 400), (400, 0), (500, 300)], 15),
    ([(0, 0), (200, 200), (400, 100), (600, 300), (800, 0), (1000, 400)], 15),
    ([(0, 0), (400, 600), (1000, 400), (1000, -400), (400, -800), (-400, -400)], 15),
    ([(0, 0), (-300, 0), (0, -300), (300,0), (200, 200), (0, 200), (-100, 100)], 15)
]

# Show graph toggle
show_graph = True

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
    end_dnc = time.time() - start
    print(f"Divide and Conquer time: {end_dnc * 1000:.2f}ms")

    # Bruteforce
    start = time.time()
    curve_bf = bezier_bruteforce(control_points=control_points, num_points=num_points)
    end_bf = time.time() - start
    print(f"Bruteforce time: {end_bf * 1000:.2f}ms")

    if show_graph:
        # Plot curve from Divide and Conquer
        x_dnc, y_dnc = zip(*curve_dnc)
        plt.plot(x_dnc, y_dnc, label=f"Bézier Curve (DnC) {end_dnc * 1000:.2f}ms", color='black')

        # Plot curve from Bruteforce
        x_bf, y_bf = zip(*curve_bf)
        plt.plot(x_bf, y_bf, label=f"Bézier Curve (Bruteforce) {end_bf * 1000:.2f}ms", color='yellow', linestyle='dashed')

        control_x, control_y = zip(*control_points)
        plt.scatter(control_x, control_y, color='red', label='Control Points')
        plt.plot(control_x, control_y, color='red', linestyle='dotted', alpha=0.5)

        plt.legend()
        plt.title(f"Test {test_num}")
        plt.show()