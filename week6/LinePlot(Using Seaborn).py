import seaborn as sns
data = sns.load_dataset("iris")
sns.lineplot(x = "sepal_length",
y = "sepal_width",data = data)