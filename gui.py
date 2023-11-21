# To Do
import tkinter as tk
import numpy as np 
from PIL import Image, ImageTk

class Command():
    def __init__(self, callback, *args):
        self.callback = callback 
        self.args = args
        
    def __call__(self):
        return self.callback(*self.args)


def draw_rectangle(canvas, llc:tuple, width, height):
    '''
    {tk.Canvas} canvas
    {tuple} llc
    '''
    return canvas.create_rectangle(
                                   llc[0]
                                   ,llc[1]
                                   ,llc[0]+width
                                   ,llc[1]+height
                                   ,fill = 'grey'
                                  )

def setGrid(canvas, shapes:list):
    for i in range(0,5):
        for j in range(0,5):
            shapes.append(draw_rectangle(canvas, (100*i,100*j),100,100))
    canvas.update()

def setGrid2(canvas):
    img = Image.fromarray(np.random.choice([0, 2, 4], 16, p=[0.8, 0.15, 0.05]).reshape(4,4))
    photo_img = ImageTk.PhotoImage(image=img)
    canvas.create_image(0, 0, image=photo_img, anchor="nw")
    
def erase_shapes(canvas, shapes):
    while shapes: # while len(shapes)>0, while shape is not empty (it is a list)
        canvas.delete(shapes.pop())

def main():
    root = tk.Tk()
    root.title('2048 Game')
    shapes = []

    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    setGrid(canvas, shapes)
    canvas.pack()

    b_erase = tk.Button(root, 
                      text = "Right",
                      command = True #Command(erase_shapes, canvas, shapes)
                      )
    b_erase.pack()

    b_erase = tk.Button(root, 
                      text = "Left",
                      command = True #Command(erase_shapes, canvas, shapes)
                      )
    b_erase.pack()

    b_erase = tk.Button(root, 
                      text = "Up",
                      command = True #Command(erase_shapes, canvas, shapes)
                      )
    b_erase.pack()

    b_erase = tk.Button(root, 
                      text = "Down",
                      command = True #Command(erase_shapes, canvas, shapes)
                      )
    b_erase.pack()

    root.mainloop()

main()