import tushare as ts
import pandas as pd
ts.set_token('88cfb35e1d9d9b50e14db2ce18ee4ada83556a7d380499a4c5ed4fa4')
pro = ts.pro_api()
pro = ts.pro_api('88cfb35e1d9d9b50e14db2ce18ee4ada83556a7d380499a4c5ed4fa4')
df = pro.moneyflow(trade_date='2019xxxx')
df.to_csv(r"D:\gupiao\fuck.csv")