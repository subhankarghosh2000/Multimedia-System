k = 2
def build_kdtree(points, depth=0):
    n = len(points)
    if n <= 0:
        return None
    axis = depth % k
    sorted_points = sorted(points, key=lambda point: point[axis])
    return {
        'point': sorted_points[n // 2],
        'left': build_kdtree(sorted_points[:n // 2], depth + 1),
        'right': build_kdtree(sorted_points[n // 2 + 1:], depth + 1)
    }
points= [[3, 6], [17, 15], [13, 15], [6, 12],[9, 1], [2, 7], [10, 19]]
kdtree = build_kdtree(points)
print(kdtree)

