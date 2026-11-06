import matplotlib.pyplot as plt
values =[5,6,3,7,2]
names =["A","B","C","D","E"]
c1 =['red','green']
c2 =['b','g','y']
plt.bar(names,values,width=0.5,color=c1)
plt.show()
plt.barh(names,values,height=0.5,color=c2)
plt.show()