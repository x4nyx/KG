import tkinter as tk
from modules import tkhelper
from modules import color_converter


class RGBWidget(tk.Frame):
    def __init__(self, dataw, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.dataw = dataw

        self.setup_widget()

    def on_submit(self):
        r = int(self.r_entry.get())
        g = int(self.g_entry.get())
        b = int(self.b_entry.get())
        self.dataw.change_rgb((int(r), int(g), int(b)))
        self.sliders_update()

    def sliders_update(self):
        self.r_slider.set(self.dataw.get("r"))
        self.g_slider.set(self.dataw.get("g"))
        self.b_slider.set(self.dataw.get("b"))

    def on_r_slider_change(self, value):
        self.dataw.change(int(value), "r")
        self.sliders_update()

    def on_g_slider_change(self, value):
        self.dataw.change(int(value), "g")
        self.sliders_update()

    def on_b_slider_change(self, value):
        self.dataw.change(int(value), "b")
        self.sliders_update()

    def setup_widget(self):
        self.r_label = tk.Label(self.master, text="R:", font=tkhelper.default_font)
        self.r_label.grid(row=0, column=0)
        self.r_entry = tk.Entry(self.master, width=3)
        self.r_entry.grid(row=0, column=1)
        self.r_slider = tk.Scale(self.master, from_=255, to=0, orient=tk.VERTICAL, command=self.on_r_slider_change)
        self.r_slider.grid(row=0, column=2, rowspan=3)
        self.g_label = tk.Label(self.master, text="G:", font=tkhelper.default_font)
        self.g_label.grid(row=1, column=0)
        self.g_entry = tk.Entry(self.master, width=3)
        self.g_entry.grid(row=1, column=1)
        self.g_slider = tk.Scale(self.master, from_=255, to=0, orient=tk.VERTICAL, command=self.on_g_slider_change)
        self.g_slider.grid(row=0, column=3, rowspan=3)
        self.b_label = tk.Label(self.master, text="B:", font=tkhelper.default_font)
        self.b_label.grid(row=2, column=0)
        self.b_entry = tk.Entry(self.master, width=3)
        self.b_entry.grid(row=2, column=1)
        self.b_slider = tk.Scale(self.master, from_=255, to=0, orient=tk.VERTICAL, command=self.on_b_slider_change)
        self.b_slider.grid(row=0, column=4, rowspan=3)
        self.submit_button = tk.Button(self.master, text="Result", command=self.on_submit)
        self.submit_button.grid(row=3, column=1, columnspan=3)
