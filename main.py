import tkinter as tk
import os

SAVE_FILE = "stitch_progress.txt"

class StitchCounterApp:
    def __init__(self, root):
        self.stitch_count = 0
        self.row_count = 0

        self.load_progress()

        root.title("🧶 Stitch Counter")
        root.configure(bg="#FFF5E1")  # Light creamy pastel background

        self.label = tk.Label(root, text=self.get_label_text(), font=("Comic Sans MS", 18), bg="#FFF5E1", fg="#8B5E3C")
        self.label.pack(pady=10)

        self.stitch_button = tk.Button(root, text="➕ Add Stitch", command=self.add_stitch, width=20, bg="#6886C5", fg="white", font=("Comic Sans MS", 12))
        self.stitch_button.pack(pady=5)

        self.row_button = tk.Button(root, text="✅ Complete Row", command=self.complete_row, width=20, bg="#6886C5", fg="white", font=("Comic Sans MS", 12))
        self.row_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="💾 Save and Quit", command=self.save_and_quit, width=20, bg="#6886C5", fg="white", font=("Comic Sans MS", 12))
        self.quit_button.pack(pady=20)

    def get_label_text(self):
        return f"🧵 Stitches: {self.stitch_count} | 📏 Rows: {self.row_count}"

    def add_stitch(self):
        self.stitch_count += 1
        self.label.config(text=self.get_label_text())

    def complete_row(self):
        self.row_count += 1
        self.stitch_count = 0
        self.label.config(text=self.get_label_text())

    def save_and_quit(self):
        with open(SAVE_FILE, "w") as file:
            file.write(f"{self.stitch_count},{self.row_count}")
        root.quit()

    def load_progress(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as file:
                data = file.read().strip()
                if data:
                    stitches, rows = map(int, data.split(","))
                    self.stitch_count = stitches
                    self.row_count = rows

def main():
    global root
    root = tk.Tk()
    app = StitchCounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
