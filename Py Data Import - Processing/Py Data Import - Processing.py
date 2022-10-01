import pandas as pd

file_input = "finance_liquor_sales.csv"
df = pd.read_csv(file_input)
#print(df.columns)

# 1
df_aggr_zc = df[["item_description", "zip_code", "bottles_sold"]].groupby(["zip_code", "item_description"]).agg({"bottles_sold": "sum"})
df_aggr_zc.to_csv("aggr_zc.csv")
#print(df_aggr_zc.head())

# 2
df_sum_store = df[["store_number", "item_description", "bottles_sold"]].groupby(["item_description", "store_number"]).agg({"bottles_sold": "sum"})
df_sum_store.rename(columns={'bottles_sold': 'store_bottles_sold'}, inplace=True)

df_sum_item = df[["item_description", "bottles_sold"]].groupby(["item_description"]).agg({"bottles_sold": "sum"})
df_sum_item.rename(columns={'bottles_sold': 'total_bottles_sold'}, inplace=True)

df_aggr = df_sum_store.join(df_sum_item, how='left', on="item_description")
df_aggr["perc"] = df_aggr["store_bottles_sold"]/df_aggr["total_bottles_sold"]*100

df_aggr.to_csv("aggr_it.csv")
#print(df_aggr.head())