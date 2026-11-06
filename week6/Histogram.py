import matplotlib.pyplot as plt
data = [12,15,20,22,23,25,25,25,30,32,35,40]
plt.hist(data, bins=5,color='skyblue',edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Valuerange")
plt.ylabel("Frequency")
plt.show()