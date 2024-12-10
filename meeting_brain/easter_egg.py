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
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill="both")
        
        # Configure style for the big red button
        style = ttk.Style()
        style.configure("Red.TButton",
                       font=("Arial", 16, "bold"),
                       padding=20,
                       background="red")
        
        # Add the big red button
        self.analyze_button = ttk.Button(
            main_frame,
            text="Analyze my Meeting",
            style="Red.TButton",
            command=self.start_analysis
        )
        self.analyze_button.pack(expand=True)
        
        # Create progress bar (hidden initially)
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        
        # Status label (hidden initially)
        self.status_label = ttk.Label(
            main_frame,
            text="",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=20)

    def start_analysis(self):
        # Disable button and show progress
        self.analyze_button.state(['disabled'])
        self.progress.pack(pady=20)
        self.progress.start(10)
        self.status_label.config(text="Analyzing meeting...")
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self.run_analysis)
        thread.start()

    def run_analysis(self):
        try:
            # Run the analysis
            asyncio.run(analyze_meeting())
            
            # Update UI on completion
            self.root.after(0, self.analysis_complete)
        except Exception as e:
            # Handle any errors
            self.root.after(0, lambda: self.analysis_complete(str(e)))

    def analysis_complete(self, error=None):
        # Stop and hide progress bar
        self.progress.stop()
        self.progress.pack_forget()
        
        if error:
            self.status_label.config(text=f"Error: {error}")
        else:
            self.status_label.config(text="Analysis Complete!")
            # Close window after 5 seconds
            self.root.after(5000, self.root.destroy)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AnalyzerGUI()
    gui.run()
