"""
CNC 逐点比较法圆弧插补计算程序

本程序用于计算指定象限和方向的圆弧插补轨迹, 支持四个象限的顺时针(cw)和逆时针(ccw)插补计算
输出包括：插补轨迹图, 插补计算过程表格, 可选的CSV文件保存

参数说明：
   - set_quadrant: 设置象限 (1, 4)
   - set_direction: 设置方向, 'cw'代表顺时针(clockwise), 'ccw'代表逆时针(counterclockwise)
   - set_x, set_y: 设置起点坐标
"""
from utils import 

if __name__ == "__main__":


    # 设置象限,方向,起点
    set_quadrant, set_direction = 4, 'cw'
    set_x, set_y = 8, 0

    points, steps = circular_interpolation(set_x, set_y, set_quadrant, set_direction)
    plot_interpolation(points, points[0], set_quadrant, set_direction)
    print_table(steps, points[0], set_quadrant, set_direction)
    save_table_to_csv(steps, points[0], set_quadrant, set_direction)
   

