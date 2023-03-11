import pyautogui
import numpy as np
import imageio

fps = 10
time = input("Time of gif  (to second) :")
time = int(time)
screen_size = pyautogui.size()
nameFile = input("Name of file : ")
output_file = nameFile +".gif"

with imageio.get_writer(output_file, mode='I', fps=fps) as writer:
    for i in range(fps * time):
        frame = np.array(pyautogui.screenshot())
        writer.append_data(frame)

print(f"Your gif saved in :  {output_file}")
