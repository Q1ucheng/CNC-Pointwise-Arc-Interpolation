################################################
# 创建了circular_interpolation函数作为调度器
# 导入此包可进行指定象限指定方向的圆弧插补计算
################################################

import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.font_manager import FontProperties

def circular_interpolation(x, y, quadrant, clockwise):
    # 根据象限和方向选择对应的插补函数
    if quadrant == 1:
        return circular_interpolation_first_cw(x, y) if clockwise == 'cw' else circular_interpolation_first_ccw(x, y)
    elif quadrant == 2:
        return circular_interpolation_second_cw(x, y) if clockwise == 'cw' else circular_interpolation_second_ccw(x, y)
    elif quadrant == 3:
        return circular_interpolation_third_cw(x, y) if clockwise == 'cw'else circular_interpolation_third_ccw(x, y)
    elif quadrant == 4:
        return circular_interpolation_fourth_cw(x, y) if clockwise == 'cw' else circular_interpolation_fourth_ccw(x, y)
    else:
        return ValueError("不是很懂")
    
    
##################################
#          顺时针插补函数          #
##################################
    
def circular_interpolation_first_cw(x, y):
    # 第一象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == y_const and y == x_const):
        if F >= 0:
            old_y = y
            y -= 1
            F = F - 2 * old_y + 1
            feed = '-Y'
        else:
            old_x = x
            x += 1
            F = F + 2 * old_x + 1
            feed = '+X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_second_cw(x, y):
    # 第二象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    # 修改终止条件
    while not (x == y_const and y == -x_const):  # 终点应为(y_const, -x_const)
        if F < 0:
            old_y = y
            y += 1  
            F = F + 2 * old_y + 1
            feed = '+Y'
        else:
            old_x = x
            x += 1
            F = F + 2 * old_x + 1
            feed = '+X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_third_cw(x, y):
    # 第三象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == y_const and y == x_const):
        if F >= 0:
            old_y = y
            y += 1
            F = F + 2 * old_y + 1
            feed = '+Y'
        else:
            old_x = x
            x -= 1
            F = F - 2 * old_x + 1
            feed = '-X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_fourth_cw(x, y):
    # 第四象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == -y_const and y == -x_const):
        if F < 0:
            old_y = y
            y -= 1
            F = F - 2 * old_y + 1
            feed = '-Y'
        else:
            old_x = x
            x -= 1
            F = F - 2 * old_x + 1
            feed = '-X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps


##################################
#          逆时针插补函数          #
##################################

def circular_interpolation_first_ccw(x, y):
    # 第一象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == y_const and y == x_const):
        if F >= 0:
            old_x = x
            x -= 1
            F = F - 2 * old_x + 1
            feed = '-X'
        else:
            old_y = y
            y += 1
            F = F + 2 * old_y + 1
            feed = '+Y'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_second_ccw(x, y):
    # 第二象限逆圆弧插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    
    while not (x == -y_const and y == -x_const): 
        if F >= 0:
            old_y = y
            y -= 1  
            F = F - 2 * old_y + 1
            feed = '-Y'
        else:
            old_x = x
            x -= 1
            F = F - 2 * old_x + 1
            feed = '-X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_third_ccw(x, y):
    # 第三象限插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == y_const and y == x_const):
        if F >= 0:
            old_x = x
            x += 1
            F = F + 2 * old_x + 1
            feed = '+X'
        else:
            old_y = y
            y -= 1
            F = F - 2 * old_y + 1
            feed = '-Y'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps

def circular_interpolation_fourth_ccw(x, y):
    # 第四象限逆时针插补
    x_const, y_const = x, y
    F = 0
    points = [(x, y)]
    steps = []
    E = abs(x_const - y_const) * 2

    step_num = 1
    while not (x == -y_const and y == -x_const):
        if F >= 0:
            old_y = y
            y += 1
            F = F + 2 * old_y + 1
            feed = '+Y'
        else:
            old_x = x
            x += 1
            F = F + 2 * old_x + 1
            feed = '+X'
        points.append((x, y))
        E -= 1
        
        steps.append({
            'step': step_num,
            'F': F,
            'feed': feed,
            'x': x,
            'y': y,
            'E': E
        })
        step_num += 1
    
    return points, steps


##################################
##          绘图函数             ##
##################################

def plot_interpolation(points, start, quadrant, clockwise='cw'):
    # 设置中文字体
    font = FontProperties(fname=r"C:/Windows/Fonts/simhei.ttf", size=12)
    
    # 存放轨迹点的坐标
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure()
    
    # 根据象限和方向绘制圆弧
    radius = np.sqrt(start[0]**2 + start[1]**2)
    if quadrant == 1:
        theta = np.linspace(0, np.pi/2, 100) if clockwise == 'cw' else np.linspace(np.pi/2, 0, 100)
    elif quadrant == 2:
        theta = np.linspace(np.pi/2, np.pi, 100) if clockwise == 'cw' else np.linspace(np.pi, np.pi/2, 100)
    elif quadrant == 3:
        theta = np.linspace(np.pi, 3*np.pi/2, 100) if clockwise == 'cw' else np.linspace(3*np.pi/2, np.pi, 100)
    elif quadrant == 4:
        theta = np.linspace(3*np.pi/2, 2*np.pi, 100) if clockwise == 'cw' else np.linspace(2*np.pi, 3*np.pi/2, 100)
    

    direction_label = '顺圆弧' if clockwise == 'cw' else '逆圆弧'
    plt.plot(radius * np.cos(theta), radius * np.sin(theta), 'b--', label=direction_label)

    # 绘制插补轨迹
    for i in range(len(xs)-1):
        plt.plot(xs[i], ys[i], 'ro', markersize=5)
        plt.plot([xs[i], xs[i+1]], [ys[i], ys[i+1]], 'r-', linewidth=2)
        plt.arrow(xs[i], ys[i], xs[i+1]-xs[i], ys[i+1]-ys[i], 
                  head_width=0.1, head_length=0.2, fc='r', ec='r', 
                  length_includes_head=True, shape='full')

    plt.plot(xs[-1], ys[-1], 'ro', markersize=5)

    plt.axis('equal')
    plt.xlabel('X', fontproperties=font)
    plt.ylabel('Y', fontproperties=font)
    
    direction_text = '顺' if clockwise == 'cw' else '逆'
    
    plt.title(f'逐点比较法第{quadrant}象限{direction_text}圆弧插补轨迹({start[0]}, {start[1]})', fontproperties=font)
    plt.grid(True)
    plt.legend(prop=font)
    plt.show()

def print_table(steps, start, quadrant, clockwise='cw'):
    # 输出表格
    direction_text = '顺' if clockwise == 'cw' else '逆'
    print(f"第{quadrant}象限{direction_text}圆弧插补计算表")
    print("| 步数 | 偏差判别 | 坐标进给 | 偏差计算 | 坐标计算 | 终点判断 |")
    print("| ---- | ---- | ---- | ---- | ---- | ---- |")
    print(f"| 起点 | NULL | NULL | F=0 | {start} | E={len(steps)} |")
    for step in steps:
        print(f"| {step['step']} | F={step['F']} | {step['feed']} | F={step['F']} | ({step['x']}, {step['y']}) | E={step['E']} |")

def save_table_to_csv(steps, start, quadrant, clockwise='cw'):
    # 保存表格到CSV文件
    direction_text = '顺' if clockwise == 'cw' else '逆'
    filename = f"逐点比较法第{quadrant}象限{direction_text}圆弧插补(起点{start}).csv"
    with open(filename, 'w', newline='', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([f'第{quadrant}象限{direction_text}圆弧插补计算表'])
        writer.writerow(['步数', '偏差判别', '坐标进给', '偏差计算', '坐标计算', '终点判断'])
        writer.writerow(['起点', 'NULL', 'NULL', 'F=0', f'{start}', f'E={len(steps)}'])
        for step in steps:
            # 在坐标进给值前添加单引号
            feed = f"'{step['feed']}"
            writer.writerow([
                step['step'],
                f"F={step['F']}",
                feed,
                f"F={step['F']}",
                f"({step['x']}, {step['y']})",
                f"E={step['E']}"
            ])
    print(f"计算结果已保存到{filename}")