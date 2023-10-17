import tkinter as tk
from tkinter import colorchooser
from widgets import rgb
from widgets import data_widget
from widgets import cmyk
from widgets import hsv


class MyApplication:
    def __init__(self, master):
        self.selected_color_label = None
        self.master = master
        master.title("Lab 1")

        self.setup_ui()

    def choose_color(self):
        color = colorchooser.askcolor(title="Select color")
        if color[0]:
            self.dataw.change_rgb(color[0])
            self.rgbw.sliders_update()
            self.cmykw.sliders_update()
            self.hsvw.sliders_update()

    def setup_ui(self):
        color_button = tk.Button(self.master, text="Select color", command=self.choose_color)
        color_button.grid(row=1,column=2, padx=20)
        self.selected_color_label = tk.Label(self.master, text="Selected color", font=("Helvetica", 14))
        self.selected_color_label.grid(row=0, column=2, padx=20)
        dataFrame = tk.Frame(self.master)
        dataFrame.grid(row=0,column=0, rowspan=2, columnspan=2, padx=20)
        dataFrame.configure(borderwidth=2, relief="solid")
        self.dataw = data_widget.DataWidget(self.selected_color_label, dataFrame)
        cmykFrame = tk.Frame(self.master)
        cmykFrame.grid(row=2, column=0, columnspan=3, pady=10)
        self.cmykw = cmyk.CMYKWidget(self.dataw, cmykFrame)
        rgbFrame = tk.Frame(self.master)
        rgbFrame.grid(row=3, column=0, columnspan=3, pady=10)
        self.rgbw = rgb.RGBWidget(self.dataw, rgbFrame)
        hsvFrame = tk.Frame(self.master)
        hsvFrame.grid(row=4, column=0, columnspan=3, pady=10)
        self.hsvw = hsv.HSVWidget(self.dataw, hsvFrame)


def main():
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
