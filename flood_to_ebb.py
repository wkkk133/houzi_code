# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:42:31 2024

@author: HP
"""

# 假设潮位数据存储在一个列表中，依次表示不同时间点的潮位变化
def flood_to_ebb(df):
    el=df['el'].rolling(window=5, min_periods=1).mean()
    df['el']=el  
    df['tide'] = df['el'].diff() > 0
    # 计算平均涨潮流速
    average_rising_speed = df[df['tide']]['mag'].mean()
    f_av=[average_rising_speed]
# 计算平均落潮流速
    average_falling_speed = df[~df['tide']]['mag'].mean()
    e_av=[ average_falling_speed]
# 计算最大涨潮流速
    max_rising_speed = df[df['tide']]['mag'].max()
    f_max=[max_rising_speed ]
    max_rising_dir = df.loc[df[df['tide']]['mag'].idxmax(), 'dir']
    f_dir=[max_rising_dir]
# 计算最大落潮流速
    max_falling_speed = df[~df['tide']]['mag'].max()
    e_max=[max_falling_speed]
    max_falling_dir = df.loc[df[~df['tide']]['mag'].idxmax(), 'dir']
    e_dir=[max_falling_dir]
# 计算全潮平均流速
    average_overall_speed = df['mag'].mean()
    a_av=[average_overall_speed ]
    if 'mmag' in df.columns and 'dmag' in df.columns:
        f_av.append(df[df['tide']]['mmag'].mean())
        f_av.append(df[df['tide']]['dmag'].mean())
        f_max.append(df[df['tide']]['mmag'].max())
        f_dir.append(df.loc[df[df['tide']]['mmag'].idxmax(), 'mdir'])
        f_max.append(df[df['tide']]['dmag'].max())
        f_dir.append(df.loc[df[df['tide']]['dmag'].idxmax(), 'ddir'])
        e_av.append(df[~df['tide']]['mmag'].mean())
        e_av.append(df[~df['tide']]['dmag'].mean())
        e_max.append(df[~df['tide']]['mmag'].max())
        e_dir.append(df.loc[df[~df['tide']]['mmag'].idxmax(), 'mdir'])
        e_max.append(df[~df['tide']]['dmag'].max())
        e_dir.append(df.loc[df[~df['tide']]['dmag'].idxmax(), 'ddir'])
        a_av.append(df['mmag'].mean())
        a_av.append(df['dmag'].mean())
    if 'dmag' in df.columns and 'mmag' not in df.columns:
        f_av.append(df[df['tide']]['dmag'].mean())
        f_max.append(df[df['tide']]['dmag'].max())
        f_dir.append(df.loc[df[df['tide']]['dmag'].idxmax(), 'ddir'])
        e_av.append(df[~df['tide']]['dmag'].mean())
        e_max.append(df[~df['tide']]['dmag'].max())
        e_dir.append(df.loc[df[~df['tide']]['dmag'].idxmax(), 'ddir'])
        a_av.append(df['dmag'].mean())
    # 输出结果
    print("平均涨潮流速:", f_av)
    print("平均落潮流速:", e_av)
    print("最大涨潮流速:", f_max,"对应流向:",f_dir)
    print("最大落潮流速:", e_max, "对应流向:", e_dir)
    print("全潮平均流速:", a_av)
    return f_av,f_max,f_dir,e_av,e_max,e_dir,a_av


