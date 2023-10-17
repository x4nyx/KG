import tkinter as tk
from modules import tkhelper
from modules import color_converter


class DataWidget(tk.Frame):
    def __init__(self, selected_color_label, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.selected_color_label = selected_color_label
        self.master = master
        self.r, self.g, self.b = 0, 0, 0
        self.c, self.m, self.y, self.k = 0, 0, 0, 0
        self.h, self.s, self.v = 0, 0, 0
        self.setup_widget()

    def setup_widget(self):
        self.cmyk_label = tk.Label(self.master, text="CMYK:(c,m,y,k)", font=tkhelper.default_font)
        self.cmyk_label.pack()
        self.rgb_label = tk.Label(self.master, text="RGB:(r,g,b)", font=tkhelper.default_font)
        self.rgb_label.pack()
        self.hsv_label = tk.Label(self.master, text="HSV:(h,s,v)", font=tkhelper.default_font)
        self.hsv_label.pack()

    def get_color_string(self):
        return color_converter.rgb_to_hex(self.r, self.g, self.b)

    def update_label(self):
        self.selected_color_label.config(bg=self.get_color_string())

    def update_data(self):
        self.cmyk_label.config(text=f"CMYK:({self.c},{self.m},{self.y},{self.k})")
        self.rgb_label.config(text=f"RGB:({self.r},{self.g},{self.b})")
        self.hsv_label.config(text=f"HSV:({self.h},{self.s},{self.v})")

    def update(self):
        self.update_label()
        self.update_data()

    def change_rgb(self, tup):
        if(len(tup) == 3):
            self.r, self.g, self.b = tup
        self.c, self.m, self.y, self.k = color_converter.rgb_to_cmyk(self.r, self.g, self.b)
        self.h, self.s, self.v = color_converter.rgb_to_hsv(self.r, self.g, self.b)
        self.update()

    def change_cmyk(self, tup):
        if(len(tup) == 4):
            self.c, self.m, self.y, self.k = tup
        self.change_rgb(color_converter.cmyk_to_rgb(self.c, self.m, self.y, self.k))

    def change_hsv(self, tup):
        if(len(tup) == 3):
            self.h, self.s, self.v = tup
        self.change_rgb(color_converter.hsv_to_rgb(self.h, self.s, self.v))

    def change(self, value, option):
        if option == "r":
            self.r = value
            self.change_rgb(())
        elif option == "g":
            self.g = value
            self.change_rgb(())
        elif option == "b":
            self.b = value
            self.change_rgb(())
        elif option == "h":
            self.h = value
            self.change_hsv(())
        elif option == "s":
            self.s = value
            self.change_hsv(())
        elif option == "v":
            self.v = value
            self.change_hsv(())
        elif option == "c":
            self.c = value
            self.change_cmyk(())
        elif option == "m":
            self.m = value
            self.change_cmyk(())
        elif option == "y":
            self.y = value
            self.change_cmyk(())
        elif option == "k":
            self.k = value
            self.change_cmyk(())

    def get(self, option):
        if option == "r":
            return self.r
        elif option == "g":
            return self.g
        elif option == "b":
            return self.b
        elif option == "h":
            return self.h
        elif option == "s":
            return self.s
        elif option == "v":
            return self.v
        elif option == "c":
            return self.c
        elif option == "m":
            return self.m
        elif option == "y":
            return self.y
        elif option == "k":
            return self.k