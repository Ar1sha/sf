import pandas as pd
orders = pd.read_csv('D:\sf\Pandas\orders\orders.csv', sep=';')
products = pd.read_csv('D:\sf\Pandas\orders\products.csv', sep=';')
products_orders = products.merge(
    orders,
    how='inner',
    
)
print(products_orders)
# mask = products_orders[products_orders['Отменен']=='Да']
# print([mask])