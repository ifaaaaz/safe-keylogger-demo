# safe_in_app_logger.py
import tkinter as tk
from datetime import datetime
from pathlib import Path

LOGFILE = Path("in_app_keylog.txt")

class SafeLoggerApp:
    def __init__(self, root):
        self.root = root
        root.title("Safe In-App Logger (Consent Required)")
        self.logging = False

        label = tk.Label(root, text="Type in the box below. Click Start to record.")
        label.pack(pady=(8,0))

        self.text = tk.Text(root, width=70, height=18)
        self.text.pack(padx=10, pady=6)
        self.text.focus_set()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(0,8))

        self.start_btn = tk.Button(btn_frame, text="Start logging (consent)", command=self.start_logging)
        self.start_btn.grid(row=0, column=0, padx=6)

        self.stop_btn = tk.Button(btn_frame, text="Stop logging", command=self.stop_logging, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=6)

        self.clear_btn = tk.Button(btn_frame, text="Clear log file", command=self.clear_log)
        self.clear_btn.grid(row=0, column=2, padx=6)

        self.status = tk.Label(root, text="Logging: OFF")
        self.status.pack(pady=(0,8))

        self.text.bind("<Key>", self.on_keypress)

    def start_logging(self):
        consent = tk.messagebox.askyesno("Consent", "Do you consent to local logging of keys typed in this app? (Yes to start)")
        if consent:
            self.logging = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.status.config(text="Logging: ON (consent given)")

    def stop_logging(self):
        self.logging = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status.config(text="Logging: OFF")

    def clear_log(self):
        if LOGFILE.exists():
            LOGFILE.unlink()
        tk.messagebox.showinfo("Log cleared", "in_app_keylog.txt removed (if it existed).")

    def on_keypress(self, event):
        char = event.char if event.char else f"<{event.keysym}>"
        timestamp = datetime.utcnow().isoformat()
        if self.logging:
            with LOGFILE.open("a", encoding="utf-8") as f:
                f.write(f"{timestamp}\t{char}\n")

if __name__ == "__main__":
    import tkinter.messagebox
    root = tk.Tk()
    app = SafeLoggerApp(root)
    root.mainloop()
