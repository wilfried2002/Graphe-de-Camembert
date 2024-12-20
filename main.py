#SCRIPT DE VISUALISATION DES DONNEE

import matplotlib.pyplot as plt

class_variable = ["chien","chat", "mouton","lapin"]
number_of_image = [10,15,8,20]
plt.pie(number_of_image,labels=class_variable)
plt.show()


