import pandas as pd
import numpy as np
lc = pd.DataFrame(pd.read_csv('LoanStats3a.csv',header=1)) #读取csv文件'LoanStats3a.csv'

#sort 函数的六种用法：
# 1）columns列名
# 2）ascending，true为升序，false为降序。默认为true
# 3）axis为排序的轴 0表示index 1表示columns
# 4）Kind快速排序
# 5）na_position对于NAN值的处理，first放在前面，last放在后面

# 一、1) 对列进行排序  比如对lc列表中列明为'loan_amount'进行排列
lc.sort(['loan_amount'],ascending=True) #按照升序排列   ascending=False降序排列
lc.sort(['loan_amount','int rate'],ascending=True)#对两列进行排序
#2) 获取前十条最大数据
lc.sort(['loan_amount'],ascending=True).head(10)#head 获取最大十条 可以通过True和False来选取后十条或者前十条

# 二、1）loc 函数   .loc函数  查询列'grade'中等于'B'的数据
lc.loc[lc['grade'] == 'B'].head(5)
#2） 除开等于外 == 也可以替换成!=
lc.loc[lc['grade'] != 'B'].head(5)
#3)进一步筛选，如'grade'== 'B'的整体列表中的几列  以下只显示['member_id', 'loan_amnt', 'grade']
lc.loc[lc['grade'] == 'B',['member_id', 'loan_amnt', 'grade']].head()
#4)对['member_id', 'loan_amnt', 'grade']中某一项进行排序 嵌套ascending = True or False等等
lc.loc[lc["grade"] == "B", ["member_id", "loan_amnt", "grade"]].sort(["loan_amnt"],ascending=False)
#5）对于多列进行同时筛选
lc.loc[(lc["grade"] == "B") & (lc["loan_amnt"]>5000), ["member_id", "term" , "loan_amnt", "grade","sub_grade", "int_rate"]].head()
lc.loc[(lc['grade'] == 'b') | (lc['loan_amnt']>5000), ["member_id", "term" , "loan_amnt", "grade","sub_grade", "int_rate"]].head()


# 三、1）求和  .sum 函数  对于'grade'=='B'与'loan_amnt'>5000的进行求和（loan_amnt之和）
lc.loc[(lc["grade"] == "B") & (lc["loan_amnt"] > 5000)].loan_amnt.sum()
# 同理还有mean()函数进行求和，count()函数进行统计,max()与min()等等函数 不在此列举