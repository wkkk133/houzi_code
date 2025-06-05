# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:21:45 2025

@author: HP
"""
# 海流流速时间序列数据
def mag_current(df):
    flow_speeds=df['mag']
    if all(speed>3 for speed in flow_speeds):  # 如果流速都大于3，可能是cm/s
        flow_speeds = flow_speeds
    else:  # 否则，假设流速单位为m/s，转换成cm/s
        flow_speeds = [speed * 100 for speed in flow_speeds]
# 定义速度段范围和计数字典
    speed_ranges = list(range(0, 101, 10))  # 速度段范围：0到100，间隔为10
    count_dict = {speed_range: 0 for speed_range in speed_ranges}

# 统计每个速度段内的数据点数量
    for speed in flow_speeds:
        for speed_range in speed_ranges:
            if  speed<=speed_range+10:
                count_dict[speed_range] += 1
                break
# 计算每个速度段的概率
    total_count = len(flow_speeds)
    probabilities = {speed_range: count / total_count for speed_range, count in count_dict.items()}
# 打印每个速度段的概率
    for speed_range, prob in probabilities.items():
        print(f"速度段 {speed_range}cm/s 以上的概率为: {prob:.2f}")
    magp=[probabilities[key] for key in probabilities]
    if 'mmag' in df.columns:
        flow_speeds=df['mmag']
        if all(speed>3 for speed in flow_speeds):  # 如果流速都大于3，可能是cm/s
            flow_speeds = flow_speeds
        else:  # 否则，假设流速单位为m/s，转换成cm/s
            flow_speeds = [speed * 100 for speed in flow_speeds]
    # 定义速度段范围和计数字典
        speed_ranges = list(range(0, 101, 10))  # 速度段范围：0到100，间隔为10
        count_dict = {speed_range: 0 for speed_range in speed_ranges}

    # 统计每个速度段内的数据点数量
        for speed in flow_speeds:
            for speed_range in speed_ranges:
                if  speed<=speed_range+10:
                    count_dict[speed_range] += 1
                    break
    # 计算每个速度段的概率
        total_count = len(flow_speeds)
        probabilities = {speed_range: count / total_count for speed_range, count in count_dict.items()}
        for speed_range, prob in probabilities.items():
            print(f"速度段 {speed_range}cm/s 以上的概率为: {prob:.2f}")
        magp.append([probabilities[key] for key in probabilities])
    if 'dmag' in df.columns:
        flow_speeds=df['dmag']
        if all(speed>3 for speed in flow_speeds):  # 如果流速都大于3，可能是cm/s
            flow_speeds = flow_speeds
        else:  # 否则，假设流速单位为m/s，转换成cm/s
            flow_speeds = [speed * 100 for speed in flow_speeds]
    # 定义速度段范围和计数字典
        speed_ranges = list(range(0, 101, 10))  # 速度段范围：0到100，间隔为10
        count_dict = {speed_range: 0 for speed_range in speed_ranges}

    # 统计每个速度段内的数据点数量
        for speed in flow_speeds:
            for speed_range in speed_ranges:
                if  speed<=speed_range+10:
                    count_dict[speed_range] += 1
                    break
    # 计算每个速度段的概率
        total_count = len(flow_speeds)
        probabilities = {speed_range: count / total_count for speed_range, count in count_dict.items()}
        for speed_range, prob in probabilities.items():
            print(f"速度段 {speed_range}cm/s 以上的概率为: {prob:.2f}")
        magp.append([probabilities[key] for key in probabilities])
    return magp 