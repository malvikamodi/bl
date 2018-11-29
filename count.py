import csv
import pandas


df = pandas.read_csv(r'resultsNew.csv')
'''
df.rename(columns={0: 'num_domains', 1: 'num_blacklisted'}, inplace=True)
df.to_csv('resultsCount.csv', index=False)

df = pandas.read_csv(r'resultsCount.csv')
'''
num_domains = df['num_domains'].sum()
num_blacklisted = df['num_blacklisted'].sum()

print(num_domains)
print(num_blacklisted)
