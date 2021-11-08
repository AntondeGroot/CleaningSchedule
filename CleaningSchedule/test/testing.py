# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:32:25 2021

@author: antondG
"""






 
from AfvalwijzerCustom import AfvalwijzerCustom
from AfvalwijzerData import AfvalwijzerData
#afvalwijzerdata = AfvalwijzerData('6851AV','41')

wijzer = AfvalwijzerCustom('6851AV','41')
data = wijzer.getData()
