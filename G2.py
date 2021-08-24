import matplotlib.pyplot as plt
c1 = [1900,2100,1400,1800]
c2 = [1600,2200,1500,1600]
years = ["2018","2019","2020","2021"]
plt.plot(years, c1, linestyle='dashed', color ='red',label='abc')
plt.plot(years,c2 , color='blue',label='xyz')
plt.legend(loc ="upper right")
plt.title("Sale Records over 2018-2021")
plt.xlabel("Sale year")
plt.ylabel("Sales in Lakhs INR")
plt.show()