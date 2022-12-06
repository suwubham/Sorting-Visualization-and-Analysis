# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random
from helper import *
plt.style.use('fivethirtyeight')

n = int(input("enter array size\n"))
a = [i for i in range(1, n+1)]
random.shuffle(a)

print("1. Megre Sort\n2. Insertion Sort\n3. Selection Sort\n4. Bubble Sort\n5. Heap Sort\n6. Quick Sort\n")
choice = int(input("Enter which sorting algorithm would you like to see?"))

if choice == 1:
    generator = mergesort(a, 0, len(a)-1)
elif choice == 2:
    generator = insertionsort(a)
elif choice == 3:
    generator = selectionsort(a)
elif choice == 4:
    generator = bubblesort(a)
elif choice == 5:
    generator = heapsort(a)
elif choice == 6:
    generator = quicksort(a, 0, len(a) - 1)

print(choice)

data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                 (1.0, 0, 0)]
    }
)
200

fig, ax = plt.subplots()

rects = ax.bar(range(len(a)), a, align="edge",
               color=color_map(data_normalizer(range(n))))


ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*len(a)))


text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]


def animate(A, rects, iteration):

    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))


anim = FuncAnimation(fig, func=animate,
                     fargs=(rects, iteration), frames=generator, interval=50,
                     repeat=False)

plt.show()
