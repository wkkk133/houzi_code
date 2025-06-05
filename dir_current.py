# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:23:34 2024

@author: HP
"""
def dir_current(df):
    import numpy as np
    from collections import Counter
    from collections import OrderedDict
    directions=df['dir']
# 定义16个方位
    sectors = [ 'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
# 每个方位的角度范围（以度为单位）
    angle_interval = 360 / len(sectors)
# 判断方位
    def get_direction_label(angle):
        index = int((angle + angle_interval / 2) // angle_interval) % len(sectors)
        return sectors[index]
# 计算每个方向的次数
    direction_labels = [get_direction_label(angle) for angle in directions]
    direction_counts = Counter(direction_labels)
    sorted_dict = OrderedDict((key, direction_counts[key]) for key in sectors if key in direction_counts)
# 计算每个方位的概率
    total = len(directions)
    probabilities = {sector: count / total*100 for sector, count in sorted_dict.items()}
    dirp=[probabilities[key] for key in probabilities]
    if 'mdir' in df.columns:
        directions=df['mdir']
        direction_labels = [get_direction_label(angle) for angle in directions]
        direction_counts = Counter(direction_labels)
        sorted_dict = OrderedDict((key, direction_counts[key]) for key in sectors if key in direction_counts)
        probabilities = {sector: count / total*100 for sector, count in sorted_dict.items()}
        dirp.append([probabilities[key] for key in probabilities])   
    if 'ddir' in df.columns:
        directions=df['ddir']
        direction_labels = [get_direction_label(angle) for angle in directions]
        direction_counts = Counter(direction_labels)
        sorted_dict = OrderedDict((key, direction_counts[key]) for key in sectors if key in direction_counts)
        probabilities = {sector: count / total*100 for sector, count in sorted_dict.items()}
        dirp.append([probabilities[key] for key in probabilities]) 
    return dirp