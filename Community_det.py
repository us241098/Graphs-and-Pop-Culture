import pandas as pd
df = pd.read_csv('gf_2_node.csv', encoding='utf8')
area_dict = dict(zip(df.Id, df.Label))
print (area_dict)

df2 = pd.read_csv('gf_2_edge.csv', encoding='utf8')
df2=df2.replace({"Source": area_dict})
df2=df2.replace({"Target": area_dict})
print (df2.head())
header = ["Source", "Target","Weight"]
df2.to_csv('output_godfather.csv', columns = header,index=False)

