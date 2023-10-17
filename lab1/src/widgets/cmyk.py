import tkinter as tk
from modules import tkhelper
from modules import color_converter


class CMYKWidget(tk.Frame):
    def __init__(self, dataw, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.dataw = dataw

        self.setup_widget()

    def on_submit(self):
        c = int(self.c_entry.get())
        m = int(self.m_entry.get())
        y = int(self.y_entry.get())
        k = int(self.k_entry.get())
        self.dataw.change_cmyk((c, m, y, k))
        self.sliders_update()

    def sliders_update(self):
        self.c_slider.set(self.dataw.get("c"))
        self.m_slider.set(self.dataw.get("m"))
        self.y_slider.set(self.dataw.get("y"))
        self.k_slider.set(self.dataw.get("k"))

    def on_c_slider_change(self, value):
        self.dataw.change(int(value), "c")
        self.sliders_update()

    def on_m_slider_change(self, value):
        self.dataw.change(int(value), "m")
        self.sliders_update()


    def on_y_slider_change(self, value):
        self.dataw.change(int(value), "y")
        self.sliders_update()

    def on_k_slider_change(self, value):
        self.dataw.change(int(value), "k")
        self.sliders_update()

    def setup_widget(self):
        self.c_label = tk.Label(self.master, text="C:", font=tkhelper.default_font)
        self.c_label.grid(row=0, column=0)
        self.c_entry = tk.Entry(self.master, width=3)
        self.c_entry.grid(row=0, column=1)
        self.c_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_c_slider_change)
        self.c_slider.grid(row=0, column=2, rowspan=4)
        self.m_label = tk.Label(self.master, text="M:", font=tkhelper.default_font)
        self.m_label.grid(row=1, column=0)
        self.m_entry = tk.Entry(self.master, width=3)
        self.m_entry.grid(row=1, column=1)
        self.m_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_m_slider_change)
        self.m_slider.grid(row=0, column=3, rowspan=4)
        self.y_label = tk.Label(self.master, text="Y:", font=tkhelper.default_font)
        self.y_label.grid(row=2, column=0)
        self.y_entry = tk.Entry(self.master, width=3)
        self.y_entry.grid(row=2, column=1)
        self.y_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_y_slider_change)
        self.y_slider.grid(row=0, column=4, rowspan=4)
        self.k_label = tk.Label(self.master, text="K:", font=tkhelper.default_font)
        self.k_label.grid(row=3, column=0)
        self.k_entry = tk.Entry(self.master, width=3)
        self.k_entry.grid(row=3, column=1)
        self.k_slider = tk.Scale(self.master, from_=100, to=0, orient=tk.VERTICAL, command=self.on_k_slider_change)
        self.k_slider.grid(row=0, column=5, rowspan=4)
        self.submit_button = tk.Button(self.master, text="Result", command=self.on_submit)
        self.submit_button.grid(row=4, column=0, columnspan=6)
