import tensorflow as tf
import numpy as np
import twstock
import json

def pred(stock_code):
    stock = twstock.Stock(stock_code)
    datas = stock.fetch_5()
    data = np.array([[[x[3], x[4], x[5], x[6], x[1]] for x in datas]])
    sql_name = "home_c" + stock_code
    price = 0
    
    with open('all_data.json') as json_file:
        con =  json.load(json_file)
    data_max = np.array(con[stock_code][0])
    data_min = np.array(con[stock_code][1])
    data = (data - data_min) / (data_max - data_min)

    model = tf.keras.models.load_model("model_save/" + sql_name + ".h5") # 讀取模型
    pred = model.predict(data)
    pred = pred * (data_max[price] - data_min[price]) + data_min[price]
    return pred[0][0]

# ['6180', '2317', '3008', '2330', '2886', '2002', '3260', '2603', '2377', '2609']
# print(pred('3008'))
    

