def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def bezier_divide_and_conquer(control_points, iterations):
    if iterations == 0:
        return [control_points[0], control_points[-1]]
    
    all_mid = [control_points]
    n = len(control_points)
    while n > 1:
        midpoints = [midpoint(all_mid[-1][i], all_mid[-1][i + 1]) for i in range(len(all_mid[-1]) - 1)]
        all_mid.append(midpoints)
        n -= 1

    first_half = [all_mid[i][0] for i in range(len(all_mid))]
    second_half = [all_mid[i][-1] for i in range(len(all_mid) - 1, -1, -1)]
    
    first_half_bezier = bezier_divide_and_conquer(first_half, iterations - 1)
    second_half_bezier = bezier_divide_and_conquer(second_half, iterations - 1)
    
    return first_half_bezier + second_half_bezier[1:]

def bezier_divide_and_conquer_animate(control_points, iterations, all_midpoints=None):
    if all_midpoints is None:
        all_midpoints = []

    if iterations == 0:
        return [control_points[0], control_points[-1]], all_midpoints
    
    all_mid = [control_points]
    n = len(control_points)
    while n > 1:
        midpoints = [midpoint(all_mid[-1][i], all_mid[-1][i + 1]) for i in range(len(all_mid[-1]) - 1)]
        all_mid.append(midpoints)
        n -= 1

    first_half = [all_mid[i][0] for i in range(len(all_mid))]
    second_half = [all_mid[i][-1] for i in range(len(all_mid) - 1, -1, -1)]
    
    all_midpoints.append(all_mid)

    first_half_bezier, all_midpoints = bezier_divide_and_conquer_animate(first_half, iterations - 1, all_midpoints)
    second_half_bezier, all_midpoints = bezier_divide_and_conquer_animate(second_half, iterations - 1, all_midpoints)
    
    return first_half_bezier + second_half_bezier[1:], all_midpoints