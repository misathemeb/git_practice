import sys
sys.path
import pandas as pd
from matplotlib import pyplot as plt

# x = [1, 3, 7]
# y = [2, 6, 12]
# plt.plot(x, y)
# plt.title('melissa\'s test data')
# plt.xlabel('homes')
# plt.ylabel('months')
# plt.legend(['homes purchased over time'])
# plt.show()

# sample_data = pd.read_csv('sample_data.csv')
#plot data
# plt.plot(sample_data.column_a, sample_data.column_b)
# plt.legend(['homes purchased'])
# plt.show()

# cdata = pd.read_csv('countries.csv')
# cdata
# #compare relative population growth btw usa and spain
# us = cdata[cdata.country == 'United States']
# us
# china = cdata[cdata.country == 'China']
# china
# plt.plot(us.year, us.population / 10**6)
# plt.plot(china.year, china.population / 10**6 )
# plt.legend(['United States', 'China'])
# plt.xlabel('year')
# plt.ylabel('population ')
# plt.show()


#relative growth %
cdata = pd.read_csv('countries.csv')
cdata

#compare  population growth btw usa and china
us = cdata[cdata.country == 'United States']
us
china = cdata[cdata.country == 'China']
china
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth first year=100')
plt.show()
