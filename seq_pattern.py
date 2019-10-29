# -*- coding: utf-8 -*-
"""
Author : LotusSmile
MIT License
"""

from pycspade.helpers import spade
from utils import make_seqData

min_support = 0.3
min_threshold = 0.5
# p_list = ['diaper', 'beer', 'noodle', 'fruit', 'meat', 'seafood', 'shampoo', 'lotion', 'coffee']
p_list = [i+101 for i in range(9)]
p_size = len(p_list) + 1
num_customers = 5
max_shopping = 3

transactions = make_seqData(num_customers, max_shopping, p_size, p_list)

for i in transactions:
    print(i)

result = spade(data=transactions, support=min_support)
for key in result.keys():
    print(key, '\n', result[key], '\n')

for mobj in result['mined_objects']:
    print(mobj)

result['seqstrm']

