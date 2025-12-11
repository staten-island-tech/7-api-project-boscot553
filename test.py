import tkinter as tk
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Functionality ---
class GraphingCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Desmos")
        
        # Entry for functions
        self.entry_label = tk.Label(root, text="Enter functions (comma separated, e.g., x, x**2, np.sin(a*x))")
        self.entry_label.pack()
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        # Button to plot
        self.plot_button = tk.Button(root, text="Plot", command=self.plot_functions)
        self.plot_button.pack()
        
        # Parameter slider button
        self.slider_button = tk.Button(root, text="Add Parameter", command=self.add_slider)
        self.slider_button.pack()
        
        # Matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
        
        self.parameters = {}  # Store sliders

    def plot_functions(self):
        funcs = self.entry.get().split(',')
        x = np.linspace(-10, 10, 500)
        self.ax.clear()
        
        # Make local dictionary for parameters
        local_dict = {'x': x, 'np': np}
        local_dict.update(self.parameters)
        
        for func_str in funcs:
            try:
                y = eval(func_str.strip(), {}, local_dict)
                self.ax.plot(x, y, label=func_str.strip())
            except Exception as e:
                print(f"Error in function '{func_str}': {e}")
        
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

    def add_slider(self):
        # Ask user for parameter name and default value
        param_name = simpledialog.askstring("Parameter", "Enter parameter name (e.g., a, b):")
        default_value = simpledialog.askfloat("Default Value", f"Enter default value for {param_name}:")
        
        if param_name:
            self.parameters[param_name] = default_value
            
            # Slider widget
            slider = tk.Scale(self.root, from_=-10, to=10, resolution=0.1,
                              orient=tk.HORIZONTAL, label=param_name,
                              command=lambda val, p=param_name: self.update_parameter(p, val))
            slider.set(default_value)
            slider.pack()
    
    def update_parameter(self, param, val):
        self.parameters[param] = float(val)
        self.plot_functions()

# --- Run App ---
root = tk.Tk()
app = GraphingCalculator(root)
root.mainloop()