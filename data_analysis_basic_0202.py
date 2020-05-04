import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import datetime, os, warnings
from pandas_datareader.data import DataReader

warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #显示负号

# 设置起始时间
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,4,30)
#print(start)
def load_data():
	if os.path.exists('000001.csv'):
		data_ss = pd.read_csv('000001.csv')
		data_kdxf = pd.read_csv('002230.csv')
	else:
		# 上证综指
		data_ss = DataReader("000001.SS", "yahoo",start,end)
		# 002230 科大讯飞 深证
		data_kdxf = DataReader("002230.SZ", "yahoo",start,end)
		data_ss.to_csv('000001.csv')
		data_kdxf.to_csv('002230.csv')
	return data_ss, data_kdxf
data_ss, data_kdxf = load_data()
# 取上证综指和科大讯飞的收盘价
close_ss = data_ss["Close"]
close_kdxf = data_kdxf["Close"]
# 将上证综指和科大讯飞进行数据合并
stock = pd.merge(data_ss, close_kdxf, left_index=True, right_index=True)
stock = stock[["Close_x","Close_y"]]
stock.columns = ["上证综指","科大讯飞"]
# 统计每日收益率
daily_return = (stock.diff()/stock.shift(periods=1)).dropna()
print(daily_return.head())

# 每日收益率可视化
fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(20,6))
daily_return["上证综指"].plot(ax=ax[0])
ax[0].set_title("上证综指")
daily_return["科大讯飞"].plot(ax=ax[1])
ax[1].set_title("科大讯飞")
plt.show()

# 散点图
fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(12,6))
plt.scatter(daily_return["科大讯飞"],daily_return["上证综指"])
plt.title("每日收益率散点图 from 科大讯飞 & 上证综指")
plt.show()

# 回归分析
daily_return["intercept"]=1.0
model = sm.OLS(daily_return["科大讯飞"],daily_return[["上证综指","intercept"]])
results = model.fit()
print(results.summary())