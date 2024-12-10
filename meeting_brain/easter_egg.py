"""
Simple GUI for Meeting Analyzer
"""

import tkinter as tk
import threading
import asyncio
import os
import sys
from run import analyze_meeting

class AnalyzerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Meeting Brain")
        
        # Center window
        window_width = 400
        window_height = 300
        x = (self.root.winfo_screenwidth() - window_width) // 2
        y = (self.root.winfo_screenheight() - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(expand=True, fill="both")
        
        # Big red button
        self.button = tk.Button(
            main_frame,
            text="Analyze my Meeting",
            font=("Arial", 16, "bold"),
            bg='#ff4444',
            fg='white',
            command=self.start_analysis
        )
        self.button.pack(expand=True, pady=20)
        
        # Status label
        self.label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            bg='white'
        )
        self.label.pack(pady=20)

    def start_analysis(self):
        self.button.config(state='disabled')
        self.label.config(text="Analyzing...")
        
        def run():
            try:
                asyncio.run(analyze_meeting())
                self.label.config(text="Done!")
                # Open the analysis file
                os.startfile('meeting_brain/outputs/summaries/analysis.txt')
                # Exit the program after 5 seconds
                self.root.after(5000, lambda: sys.exit(0))
            except:
                self.label.config(text="Error occurred")
                self.button.config(state='normal')
        
        threading.Thread(target=run, daemon=True).start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AnalyzerGUI()
    gui.run()
