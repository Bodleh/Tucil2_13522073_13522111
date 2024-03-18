from typing import Tuple, List

def midpoint(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def bezier_divide_and_conquer(
    control_points: List[Tuple[int, int]], 
    iterations: int
) -> List[Tuple[int, int]]:
    if iterations == 0:
        return [control_points[0], control_points[-1]]
    else:
        first_half = [control_points[0]]
        second_half = [control_points[-1]]
        for _ in range(len(control_points), 1, -1):
            midpoints = [midpoint(control_points[i], control_points[i + 1]) for i in range(len(control_points) - 1)]
            control_points = midpoints
            first_half.append(midpoints[0])
            second_half.insert(0, midpoints[-1])
        
        first_half_bezier = bezier_divide_and_conquer(first_half, iterations - 1)
        second_half_bezier = bezier_divide_and_conquer(second_half, iterations - 1)
        return first_half_bezier + second_half_bezier[1:]

def bezier_divide_and_conquer_animate(
    control_points: List[Tuple[int, int]], 
    iterations: int, 
    all_midpoints: List[List[List[Tuple[int, int]]]] | None = None
) -> Tuple[List[Tuple[int, int]], List[List[List[Tuple[int, int]]]]]:
    if all_midpoints is None:
        all_midpoints = []

    if iterations == 0:
        return [control_points[0], control_points[-1]], all_midpoints
    else:
        all_mid = [control_points]
        first_half = [control_points[0]]
        second_half = [control_points[-1]]
        for _ in range(len(control_points), 1, -1):
            midpoints = [midpoint(control_points[i], control_points[i + 1]) for i in range(len(control_points) - 1)]
            all_mid.append(midpoints)
            control_points = midpoints
            first_half.append(midpoints[0])
            second_half.insert(0, midpoints[-1])
        
        all_midpoints.append(all_mid)

        first_half_bezier, all_midpoints = bezier_divide_and_conquer_animate(first_half, iterations - 1, all_midpoints)
        second_half_bezier, all_midpoints = bezier_divide_and_conquer_animate(second_half, iterations - 1, all_midpoints)
        
        return first_half_bezier + second_half_bezier[1:], all_midpoints

def de_casteljau(points: List[Tuple[int, int]], t: float) -> Tuple[int, int]:
    if len(points) == 1:
        return points[0]
    else:
        new_points = []
        for i in range(len(points) - 1):
            new_point = ((1 - t) * points[i][0] + t * points[i + 1][0], (1 - t) * points[i][1] + t * points[i + 1][1])
            new_points.append(new_point)
        return de_casteljau(new_points, t)

def bezier_bruteforce(control_points: List[Tuple[int, int]], iterations: int) -> List[Tuple[int, int]]:
    curve_points = []
    num_points = 2 ** iterations + 1
    for i in range(num_points):
        t = i / (num_points - 1)
        curve_points.append(de_casteljau(control_points, t))
    return curve_points