import tkinter as tk

window = tk.Tk()

temp_img = tk.PhotoImage(file='BackgroundRemover/images/appart.png')
zx = int(640 / temp_img.width())
zy = int(480 / temp_img.height())
background_img = temp_img.zoom(zx, zy)

can = tk.Canvas(window, width=640, height=480)
can.pack()

can.create_image(320, 240, image=background_img)

window.mainloop()
