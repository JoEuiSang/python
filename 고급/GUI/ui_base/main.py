import tkinter as tk
import 고급.GUI.ui_메모장.fileRW as f
import 고급.GUI.ui_메모장.main_ui as ui



def main():
    root = tk.Tk()
    file = f.FileRW('./filelist')
    app = ui.AppWindow(root, '650x500+100+100', file)
    app.mainloop()

main()