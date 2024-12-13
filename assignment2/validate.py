import re
from shapely import wkt
import matplotlib.pyplot as plt


def validate_wkt_file(filename):
    squares = []
    orders = set()
    areas = []

    with open(filename, 'r') as f:
        next(f)  # Skip header
        for line in f:
            wkt_str, order, area = line.strip().split(';')
            polygon = wkt.loads(wkt_str)
            squares.append(polygon)
            orders.add(int(order))
            areas.append(float(area))

    # 检查顺序
    print(f"Orders present: {sorted(orders)}")

    # 检查面积
    print(f"Min area: {min(areas)}, Max area: {max(areas)}")

    # 简单可视化
    fig, ax = plt.subplots()
    for square in squares:
        x, y = square.exterior.xy
        ax.plot(x, y, color='blue')

    ax.set_aspect('equal', 'box')
    plt.title("Pythagoras Tree Visualization")
    plt.show()


# 使用方法
validate_wkt_file('out.wkt')