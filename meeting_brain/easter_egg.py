"""
Easter Egg GUI for Meeting Analyzer
"""

import tkinter as tk
from tkinter import ttk
import threading
import time
import asyncio
from run import analyze_meeting

class AnalyzerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Meeting Brain")
        
        # Set window size and center it
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Create main frame with padding
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg='white')
        main_frame.pack(expand=True, fill="both")
        
        # Add the big red button
        self.analyze_button = tk.Button(
            main_frame,
            text="Analyze my Meeting",
            font=("Arial", 16, "bold"),
            bg='#ff4444',
            fg='white',
            activebackground='#cc3333',
            activeforeground='white',
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            command=self.start_analysis
        )
        self.analyze_button.pack(expand=True, pady=20)
        
        # Create progress bar (hidden initially)
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        
        # Status label (hidden initially)
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            bg='white'
        )
        self.status_label.pack(pady=20)

    def start_analysis(self):
        # Disable button and show progress
        self.analyze_button.config(state='disabled')
        self.progress.pack(pady=20)
        self.progress.start(10)
        self.status_label.config(text="Analyzing meeting...")
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self.run_analysis)
        thread.daemon = True
        thread.start()

    def run_analysis(self):
        try:
            # Run the analysis
            asyncio.run(analyze_meeting())
            self.root.after(0, self.on_success)
        except Exception as error:
            self.root.after(0, lambda: self.on_error(str(error)))

    def on_success(self):
        # Stop and hide progress bar
        self.progress.stop()
        self.progress.pack_forget()
        self.status_label.config(text="Analysis Complete!")
        # Close window after 5 seconds
        self.root.after(5000, self.root.destroy)

    def on_error(self, error_msg):
        # Stop and hide progress bar
        self.progress.stop()
        self.progress.pack_forget()
        self.status_label.config(text=f"Error: {error_msg}")
        self.analyze_button.config(state='normal')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AnalyzerGUI()
    gui.run()
