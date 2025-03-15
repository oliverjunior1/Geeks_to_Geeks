import matplotlib.pyplot as plt

x = [35, 25,25,15]
y = ['Python', 'Javascript', 'Java', 'C#']

plt.pie(x, labels=y, autopct="%0.0f%%")
plt.title("The four most important languages around the World!")
plt.show()

