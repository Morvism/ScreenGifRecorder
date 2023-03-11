import pyautogui
import numpy as np
import imageio
import easygui


fps = 10
time = input("Time of gif  (to second) :")
time = int(time)
screen_size = pyautogui.size()
output_folder = easygui.diropenbox()
output_file_name = easygui.enterbox("Enter the output file name")

output_file = output_folder  + "/" + output_file_name + ".gif"

with imageio.get_writer(output_file, mode='I', fps=fps) as writer:
    for i in range(fps * time):
        frame = np.array(pyautogui.screenshot())
        writer.append_data(frame)

print(f"Your gif saved in :  {output_file}")
