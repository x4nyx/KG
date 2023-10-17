import tkinter as tk
from modules import tkhelper
from modules import color_converter


class HSVWidget(tk.Frame):
    def __init__(self, dataw, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.dataw = dataw

        self.setup_widget()

    def on_submit(self):
        h = int(self.h_entry.get())
        s = int(self.s_entry.get())
        v = int(self.v_entry.get())
        self.dataw.change_hsv((int(h), int(s), int(v)))
        self.sliders_update()

    def sliders_update(self):
        self.h_slider.set(self.dataw.get("h"))
        self.s_slider.set(self.dataw.get("s"))
        self.v_slider.set(self.dataw.get("v"))

    def on_h_slider_change(self, value):
        self.dataw.change(int(value), "h")
        self.sliders_update()

    def on_s_slider_change(self, value):
        self.dataw.change(int(value), "s")
        self.sliders_update()

    def on_v_slider_change(self, value):
        self.dataw.change(int(value), "v")
        self.sliders_update()

    def setup_widget(self):
        self.h_label = tk.Label(self.master, text="H:", font=tkhelper.default_font)
        self.h_label.grid(row=0, column=0)
        self.h_entry = tk.Entry(self.master, width=3)
        self.h_entry.grid(row=0, column=1)
        self.h_slider = tk.Scale(self.master, from_=360, to=0, orient=tk.VERTICAL, command=self.on_h_slider_change)
        self.h_slider.grid(row=0, column=2, rowspan=3)
        self.s_label = tk.Label(self.master, text="S:", font=tkhelper.default_font)
        self.s_label.grid(row=1, column=0)
        self.s_entry = tk.Entry(self.master, width=3)
        self.s_entry.grid(row=1, column=1)
        self.s_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_s_slider_change)
        self.s_slider.grid(row=0, column=3, rowspan=3)
        self.v_label = tk.Label(self.master, text="V:", font=tkhelper.default_font)
        self.v_label.grid(row=2, column=0)
        self.v_entry = tk.Entry(self.master, width=3)
        self.v_entry.grid(row=2, column=1)
        self.v_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_v_slider_change)
        self.v_slider.grid(row=0, column=4, rowspan=3)
        self.submit_button = tk.Button(self.master, text="Result", command=self.on_submit)
        self.submit_button.grid(row=3,column=1, columnspan=3)
