# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:29:18 2024

@author: HP
"""
from datetime import datetime

def datetime_to_matlab(dtime):
    # MATLAB的0日期是0000-01-01，而Python的datetime的0日期是1970-01-01
    matlab_datenum_offset = 719529  # 从1970-01-01至0000-01-01的天数差
    
    # 将datetime对象转换为自1970-01-01以来的天数
    delta = dtime - datetime(1970, 1, 1)
    return delta.dt.days + delta.dt.seconds / 86400 + matlab_datenum_offset