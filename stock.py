import tushare as ts
import pandas as pd
import datetime
import numpy as np
#设置tushare token
ts.set_token('058a81af5174d91a9c4c651e603168e91ddf35b26e6cadfa0d8f34bb')
pro = ts.pro_api()
pro = ts.pro_api('058a81af5174d91a9c4c651e603168e91ddf35b26e6cadfa0d8f34bb')
#基础参数
ts_code = input('请输入TS代码：')
now = datetime.datetime.now()
past = now + datetime.timedelta(days=-365)
start_date = past.strftime('%Y%m%d')
end_date = now.strftime('%Y%m%d')
share_name = pro.namechange(ts_code=ts_code)
share_name = share_name['name'][0]
filename = share_name+'一年持仓比例与收盘价占比'
print(start_date)
print(end_date)
print(share_name)
#资金占比
daily_ratio = pro.hk_hold(start_date=start_date,end_date=end_date,ts_code=ts_code)
daily_ratio = daily_ratio.sort_values(['trade_date'], ascending = True)
daily_ratio = daily_ratio.drop(['code','ts_code','vol','exchange'], axis = 1)
#收盘价格
daily_close_price = pro.daily(start_date=start_date,end_date=end_date,ts_code=ts_code)
daily_close_price = daily_close_price.sort_values(['trade_date'], ascending = True)
daily_close_price = daily_close_price[['trade_date','close']]
daily_close_price = pd.DataFrame(daily_close_price)
#列表融合
daily_change = daily_ratio.merge(daily_close_price, on='trade_date', how='left')
#绘制图像
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei']#rc配置为黑体字体    SimHei黑体字体    显示中文标签
plt.rcParams['font.serif'] = ['SimHei']#rc配置为黑体字体    SimHei黑体字体
plt.rcParams['axes.unicode_minus'] = False #axes.unicode_minus显示为负数， False代表全是正数
fig1 = plt.figure(figsize=(8, 6))
ax = fig1.add_subplot()
ax.grid()
xmajorLocator = MultipleLocator(45)
ax.plot(daily_change['trade_date'],daily_change['ratio'],'-',color='b',label='持仓比例')
ax.xaxis.set_major_locator(xmajorLocator)
ax2 = ax.twinx()
ax2.plot(daily_change['trade_date'],daily_change['close'],'o',color='r',label='收盘价格')
ax.xaxis.set_major_locator(xmajorLocator)
ax.set_xlabel('日期',fontsize=16)
ax.set_ylabel('持仓比例（%）',fontsize=16,color='b')
ax2.set_ylabel('收盘价格（元）',fontsize=16,color='r')
ax.set_title(ts_code+share_name,fontsize=16)
plt.savefig(filename+'.png')
plt.show()
#输出文件
filename = share_name+'一年持仓比例与收盘价占比'
daily_change.to_csv(filename+'.csv', encoding='utf-8-sig')
