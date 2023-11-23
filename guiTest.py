import tkinter as tk
import numpy as np
from main import *

# Try with pygame ?

# Fonction pour mettre à jour les données et afficher un nouveau tableau
def update_data_right(starting_grid):
    new_data = movementRight(starting_grid.copy())

    if (new_data==starting_grid).all():
            pass
    else:
            starting_grid = addRandomToGrid(new_data)

    tableau_formatte = '\n'.join(['\t'.join(map(str, row)) for row in starting_grid])
    text_widget.delete('1.0', tk.END)  # Efface le contenu actuel
    text_widget.insert('1.0', tableau_formatte)  # Affiche les nouvelles données

# Créez une fenêtre Tkinter
root = tk.Tk()
root.title("Affichage d'un tableau NumPy")

# Créez un widget Text pour afficher le tableau
text_widget = tk.Text(root, height=20, width=40)
text_widget.pack()

# Créez un bouton pour mettre à jour les données
starting_numbers = [0, 2, 4]
starting_grid = np.random.choice(starting_numbers, 16, p=[0.8, 0.15, 0.05]).reshape(4,4)

update_right = tk.Button(root, text="Mettre à jour les données", command=lambda: update_data_right(starting_grid))
update_right.pack()

# Initialise le widget Text avec les données initiales
tableau_formatte = '\n'.join(['\t'.join(map(str, row)) for row in starting_grid])
text_widget.insert('1.0', tableau_formatte)

# Lancez la boucle principale de Tkinter
root.mainloop()

# 
