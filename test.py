from bezier_curve import bezier_divide_and_conquer, bezier_bruteforce
import time
import matplotlib.pyplot as plt

test1= [(0, 0), (100, 200), (300, 300), (500, 0), (300, -300), (-100, -200), (-200, 100)]
test2 = [(0, 0), (100, 200), (300, 0)]
iterations = 20

control_points = test1

num_points = 3
for i in range(iterations - 1) :
    num_points += num_points - 1

print(num_points)

start = time.time()
curve_dnc = bezier_divide_and_conquer(control_points=control_points, iterations=iterations)
end = time.time() - start
print(f"Divide and Conquer time: {end * 1000}ms")

start = time.time()
curve_bf = bezier_bruteforce(control_points=control_points, num_points=num_points)
end = time.time() - start
print(f"Bruteforce time: {end * 1000}ms")

# Plot curve
x, y = zip(*curve_bf)
plt.plot(x, y, label='Bézier Curve')

# Plot control points
control_x, control_y = zip(*control_points)
plt.scatter(control_x, control_y, color='red', label='Control Points')
plt.plot(control_x, control_y, color='red', linestyle='dashed', alpha=0.5)

plt.legend()
plt.show()