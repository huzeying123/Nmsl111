import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


#定义函数读取数据
#思路为由pandas读取csv文件  构建zip的循环来读取得到数据的list
#注意此处得到的是由series转换成的list
#关键函数  read_csv()  zip()  for 循环 list

def get_data(self):
    data = pd.read_csv(self)
    x_parameter = []
    y_parameter = []
    for singal_square_feet, single_price_value in zip(data['square_feet'],data['price']):    #利用循环与zip函数 读取数据
        x_parameter.append([float(singal_square_feet)])
        y_parameter.append(float(single_price_value))
    return x_parameter , y_parameter

#转换格式
#由于新版的sklearn只接受二维array  所以我们需要用上述得到的list先转换成numpy的array 然后再利用reshape()函数进行处理成为二维
#关键函数  np.asarray()  reshape(-1,1)
def list2array(self):
    array = np.asarray(self).reshape(-1,1)
    return array


#利用Linear Regression 进行训练
#通过linear_model.LinearRegression()函数的 fit() predict() intercept_ coef_ 等函数进行拟合、预测、得到截距和斜率
def linear_model_main(x_parameters , y_parameters , predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(x_parameters , y_parameters)
    predict_outcome = regr.predict(predict_value)
    prediction = {}
    prediction['intercept'] = regr.intercept_
    prediction['coefficency'] = regr.coef_
    prediction['predicted_value'] = predict_outcome
    return prediction

#输出过程
X,Y = get_data('input_data.csv')
predictvalue = 700
X = list2array(X)
Y = list2array(Y)
predictvalue = list2array(predictvalue)
print(X)
print(Y)
print(predictvalue)
result = linear_model_main(X,Y,predictvalue)
print('intercept value:',result['intercept'])
print('coefficency value:',result['coefficency'])
print('predicted value:',result['predicted_value'])

#利用latplotlib绘制图形过程
def show_gragh(x_parameter,y_parameter):
    regr = linear_model.LinearRegression()
    regr.fit(x_parameter,y_parameter)
    plt.scatter(x_parameter,y_parameter,color='blue')
    plt.plot(x_parameter,regr.predict(x_parameter),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

show_gragh(X,Y)
