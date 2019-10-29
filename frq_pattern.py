# -*- coding: utf-8 -*-
"""
Author : LotusSmile
MIT License
"""

import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import matplotlib.pyplot as plt
import seaborn as sns
from utils import make_Data

# before start
p_list = ['diaper', 'beer', 'noodle', 'fruit', 'meat', 'seafood', 'shampoo', 'lotion', 'coffee']
p_size = len(p_list) + 1
total_customers = 10
min_support = 0.3
min_threshold = 0.5

# to make random virtual transactions of customers
transactions = make_Data(total_customers, p_size, p_list)

# to get the transaction result
for customer in transactions:
    print(customer)

# to make transaction encoder
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary.astype("int"), columns=te.columns_)

# to get frequent itemsets using the apriori
frq_itemsets = apriori(df, min_support=min_support, use_colnames=True)
print(frq_itemsets)

# to get frequent itemsets using the fp-growth
frq_itemsets2 = fpgrowth(df, min_support=min_support, use_colnames=True)
print(frq_itemsets2)

# to get association rules
ar = association_rules(frq_itemsets, metric="confidence", min_threshold=min_threshold)
print(ar)
ar2 = association_rules(frq_itemsets2, metric="confidence", min_threshold=min_threshold)
print(ar2)

# to make plot using seaborn
histogram = np.sum(df)
x_label = histogram.index.to_list()
y_label = "Sales"
y = histogram.values.tolist()
sns.barplot(x=x_label, y=y, ci=None)
# plt.ylim(0, 10)
plt.ylabel(y_label)
plt.title("Sales by Products")
plt.show()