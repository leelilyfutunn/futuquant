# -*- coding: utf-8 -*-
"""
定时重启富途牛牛程序
"""
import psutil
import time
import os


def get_process_by_name(namestr):
    """通过名称获取进程"""
    for pid in psutil.pids():
        process = psutil.Process(pid)
        name = process.name()
        if name == namestr:
            return process
    return None

if __name__ == '__main__':
    # 设置重启时间，时：分
    restart_time_str = '19:40'
    restart_time = time.strptime(restart_time_str, '%H:%M')
    ftnn_path = 'C:\Program Files (x86)\FTNN\FTNN.exe'
    while True:
        cur_time = time.localtime()
        print('current time is {}'.format(
            time.strftime('%Y-%m-%d %H:%M:%S', cur_time)))
        if cur_time.tm_hour == restart_time.tm_hour and\
                cur_time.tm_min == restart_time.tm_min:
            print('{}:time to restart'.format(
                time.strftime('%Y-%m-%d %H:%M:%S', cur_time)))
            ftnn_process = get_process_by_name('FTNN.exe')
            if ftnn_process is not None:
                ftnn_process.kill()
            os.popen(ftnn_path)
        time.sleep(60)
