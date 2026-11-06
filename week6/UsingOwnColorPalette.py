import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
c_p = {'Male': 'lightblue', 'Female': 'pink'}
sns.pairplot(data,hue='sex',palette=c_p)
plt.show()