#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #Загрузка библиотеки для математических операций.
import numpy #Загрузка библиотеки для более сложных функций.
import matplotlib.pyplot as mpp #Загрузка библиотеки для построения графиков (которая в коде называется mpp).

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1) #Создание массива значений a, от которых будем вычислять y(a) из чисел от 0 до 200 с шагом 0.1.
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #При помощи matplotlib строим график sin(a)*sin(a/20) для каждого a.
    )
    mpp.show()#Отобразить построенное.