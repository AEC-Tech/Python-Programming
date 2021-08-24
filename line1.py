import matplotlib.pyplot as plt
years = [2016,2017,2018,2019,2020,2021]
sales = [9000,12000,11500,13000,10000,9200]
plt.plot(years,sales,color='red')
plt.ylim((5000,15000))
plt.title("Sale Report")
plt.show()