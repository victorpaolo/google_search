# -*- coding: utf-8 -*-
from pytrends.request import TrendReq
import pandas as pd
from PytrendsAddon import interest_by_city


pytrends = TrendReq(hl='es-ES')
keywords = ["residencia", "empleo", "familia", "domicilio", "hogar"]

pytrends.build_payload(keywords,
                       timeframe='now 7-d',
                       geo="ES")
data1 = pytrends.interest_over_time()
data2 = data1.drop('isPartial', axis=1)
print(data2)

interest_by_city(pytrends)

def related_queries():
    data = pytrends.related_queries()
    for kw in keywords:
        print(kw + ' top queries: ')
        print(data[kw]['top'].head(30))
        print('')

data6 = related_queries()
