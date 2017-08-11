# -*- coding: utf-8 -*-
"""
验证接口：获取某个市场的全部快照数据
"""
from futuquant.open_context import *

import time


def loop_get_mkt_snapshot(api_svr_ip, api_svr_port, market):
    """
    验证接口：获取某个市场的全部快照数据 get_mkt_snapshot
    :param api_svr_ip: (string)ip
    :param api_svr_port: (int)port
    :param market: market type
    :return:
    """
    # 创建行情api
    quote_ctx = OpenQuoteContext(host=api_svr_ip, port=api_svr_port)
    stock_type = ['STOCK', 'IDX', 'ETF', 'WARRANT', 'BOND']

    while True:
        stock_codes = []
        # 枚举所有的股票类型，获取股票codes
        for sub_type in stock_type:
            ret_code, ret_data = quote_ctx.get_stock_basicinfo(market, sub_type)
            if ret_code == 0:
                for ix, row in ret_data.iterrows():
                    stock_codes.append(row['code'])

        if len(stock_codes) == 0:
            quote_ctx.close()
            print("Error market:'{}' can not get stock info".format(market))
            return

        # 按频率限制获取股票快照: 每5秒200支股票
        for i in range(1, len(stock_codes), 200):
            print("from {}, total {}".format(i, len(stock_codes)))
            ret_code, ret_data = quote_ctx.get_market_snapshot(stock_codes[i:i+200])
            if ret_code != 0:
                print(ret_code, ret_data)
            time.sleep(5)
        time.sleep(10)

if __name__ == "__main__":
    API_SVR_IP = '127.0.0.1'
    API_SVR_PORT = 11111
    MARKET = 'US'  # 'US'/'SH'/'SZ'
    loop_get_mkt_snapshot(API_SVR_IP, API_SVR_PORT, MARKET)
