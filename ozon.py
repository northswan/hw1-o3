#!/usr/bin/env python3

import argparse
from scipy.io import netcdf
import numpy as np
import json
import matplotlib.pyplot as plt
import re

parser = argparse.ArgumentParser()
parser.add_argument('longitude', metavar='LON', type=float, help='Longitude, deg')
parser.add_argument('latitude',  metavar='LAT', type=float, help='Latitude, deg')

def month_ozon(value):
    st = {
        'min': float(np.min(value)),
        'max': float(np.max(value)),
        'mean': float(np.round(np.mean(value), 1))
    }
    return st
def month(value, t, month):
    index = []
    for i in range(len(t)):
        if (t[i]-t[0]) % 12 == month-1:
            index.append(i)
    return value[index], index

def graph_plot(ozon, time, jan_ind, jul_ind, out_graph):
    plt.figure(figsize = (12, 8))
    plt.plot(np.array(time)-np.array(time)[0], ozon, label = 'Озон за все время', color = 'red')
    plt.plot(np.array(time)[jan_ind]-np.array(time)[0], ozon[jan_ind], label = 'Озон за январи', color = 'blue')
    plt.plot(np.array(time)[jul_ind]-np.array(time)[0], ozon[jul_ind], label = 'Озон за июли', color = 'green')
    plt.grid()
    plt.xlabel('Месяцы начиная с 1970-01-15 00:00:00.0')
    plt.ylabel('Содержание озона')
    plt.title('Содержание озона в атмосфере Земли')
    plt.legend()
    plt.savefig(out_graph)




if __name__ == "__main__":
    args = parser.parse_args()

    #print(args.longitude, args.latitude)
    with netcdf.netcdf_file('MSR-2.nc') as netcdf_file:
        data = netcdf_file.variables
        ozon = data['Average_O3_column'].data
        lat  = data['latitude'].data
        long = data['longitude'].data
        time = data['time'].data
    #найдем координаты, ближайшие к заданным
    lat_giv = (np.abs(lat-args.latitude)).argmin()
    long_giv = (np.abs(long-args.longitude)).argmin()

    #значение озона для заданных координат
    ozon_value = ozon[:, lat_giv, long_giv]
    
    #значение озона в январе и июне
    jan_value, jan_index = month(ozon_value, time, 1)
    jul_value, jul_index = month(ozon_value, time, 7)

    #min, max, mean значения озона
    all_ozon = month_ozon(ozon_value)
    jan_ozon = month_ozon(jan_value)
    jul_ozon = month_ozon(jul_value)
    #print('1', coord)
    #запись в файл
    statistic = {
        "coordinates": [args.longitude, args.latitude],
        "jan": jan_ozon,
        "jul": jul_ozon,
        "all": all_ozon
    }
    with open('ozon.json', 'w') as f:
        json.dump(statistic, f, indent=2)

    #построение графика
    graph_plot(ozon_value, time, jan_index, jul_index, 'ozon.png')


