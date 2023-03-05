import pandas as pd
print("#########################  data set  ##########################################")
df_csv = pd.read_csv('universities_rankings.csv')
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
print(df_csv)
print("#########################  Q1(1)  ##########################################")
del df_csv["link"]
del df_csv["logo"]
del df_csv["city"]
print(df_csv)

print("#########################  Q1(2)  ##########################################")
print("#########################  Before  ##########################################")
for col in df_csv.columns:
    print(col)

df_csv.rename(columns = {'student_faculty_ratio':'std_fac_ratio', 'international_students':'inter_stds'}, inplace = True)
print("#########################  After  ##########################################")
for col in df_csv.columns:
    print(col)

print("#########################  Q1(3)  ##########################################")
new_data=df_csv.nsmallest(400,'year')
# new_data=new_data.dropna()
print(new_data)