import random
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def Zadacha_1():
    #Задача 1. Постройте график функции
    #𝑓 𝑥 = 5𝑥^2+10x-30
    #определите, при каких значения x значение функции отрицательно.
 
    x = arange(-10, 10, .01)
    y = 5*x**2 + 10*x - 30
    
    plt.plot(x,y,color ='r')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    
    result = []
    for el in x:
        y_cor = 5*el**2 + 10*el - 30
        if(y_cor<0):
            result.append(el)
    x_start ="["+str(round(result[0],1))+","+str(round(result[-1],1))+"]"
    plt.text(5, 500, x_start)
    plt.show()


def Zadacha_2():
    dom_name = ('d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14','d15')
    square_d = [] 
    price_d = []
    for _ in range(15):
        num1 = randint(100,300)
        square_d.append(num1)
    print (f'Наименования домов: {dom_name}')
    print(f'Площадь домов: {square_d}')
    for _ in range(15):
        num2= randint(3000000,20000000)
        price_d.append(num2)
    print(f'Стоимость домов: {price_d}')

    price_mkv =[]
    for price in range(len(price_d)):
        price_mkv.append(int(price_d[price]/square_d[price]))
   
    catalog_dom = {}
    for i in range (len(dom_name)):
        if price_mkv[i] < 50000:
            catalog_dom.update({square_d[i]: (dom_name[i],price_mkv[i])})
    sorted_catalog = dict(sorted(catalog_dom.items()))
    values = []
    for key,value in sorted_catalog.items():
        values.append(value)
    for el in range(len(values)):
            print (f'Подходящие варианты: дом: {values[el][0]}, цена за кв.метр: {values[el][1]}')

    y_pos = np.arange(len(dom_name))
    ax = plt.gca()
    ax.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
    ax.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)
    plt.bar(y_pos, price_mkv, align='center', alpha=1)
    plt.xticks(y_pos, dom_name)
    plt.ylabel('Рубли')
    plt.title('Стоимость кв.метра')
    plt.show()
Zadacha_1()

#Zadacha_2() 

