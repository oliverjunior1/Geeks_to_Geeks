import matplotlib.pyplot as plt

code = ['Python', 'Javascript', 'Java', 'C#', "Nocode", "Others"]
percent = [25,20,16,10,9,19]

plt.pie(percent, labels=code)

plt.show()

