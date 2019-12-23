import tushare as ts
ts.set_token('058a81af5174d91a9c4c651e603168e91ddf35b26e6cadfa0d8f34bb')
pro = ts.pro_api()
pro = ts.pro_api('058a81af5174d91a9c4c651e603168e91ddf35b26e6cadfa0d8f34bb')
data = '20191219'
df = pro.hk_hold(trade_date='20191219')
df.columns = ['交易所代码','交易日期','TS交易所代码','名称','持股数量（股）','持股占比','类型']
print(df)
df.to_csv(r'D:\北上资金明细\北上资金明细20191219.csv', encoding='utf-8-sig')