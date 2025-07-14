import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox, filedialog
import sys
import os
from PIL import Image, ImageTk

def creating():
    window = tk.Tk()
    window.title('VIX editor')
    window.geometry('680x480')

    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Untitled.PNG')

    try:
        window.iconbitmap(icon_path)
    except tk.TclError:
        try:
            photo = Image.open(icon_path)
            photo = ImageTk.PhotoImage(photo)
            window.wm_iconphoto(True, photo)

            photo = tk.PhotoImage(file=icon_path)
            window.iconphoto(True, photo)

        except Exception as e:
            pass

    label = tk.Label(window, text='Welcome to VIX editor! you can exit with Esc :) ')
    label.pack()

    style = ttk.Style()
    style.theme_use('clam')
    window.configure(bg='black')

    text_area = scrolledtext.ScrolledText(window,
                                          wrap=tk.WORD,
                                          font=('consolas', 12),
                                          bg='black',
                                          fg='#00FF00',
                                          padx=10,
                                          pady=10,
                                          insertbackground='#00FF00',
                                          insertwidth=2,
                                          undo=True)
    text_area.pack(expand=True, fill='both')

    current_filepath = None

    def open_file(filepath_to_open=None):
        nonlocal current_filepath

        if filepath_to_open:
            filepath = filepath_to_open
        else:
            filetypes = [
                ('All files', '*.*'),
                ('Text files', '*.txt'),
                ('Python files', '*.py')
            ]
            filepath = filedialog.askopenfilename(filetypes=filetypes)

        if filepath:
            try:
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                        text_area.delete("1.0", tk.END)
                        text_area.insert("1.0", content)
                    current_filepath = filepath
                    window.title(f'VIX editor - {filepath}')
                    text_area.edit_reset()
                else:
                    text_area.delete("1.0", tk.END)
                    current_filepath = filepath
                    window.title(f'VIX editor - {filepath} (New File)')
                    messagebox.showinfo("New File", f"File '{filepath}' does not exist. Starting new file.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open/create file: {e}")
                current_filepath = None

    def save_file():
        nonlocal current_filepath
        
        if current_filepath:
            filepath = current_filepath
        else:
            filetypes = [
                ('Text files', '*.txt'),
                ('Python files', '*.py'),
                ('All files', '*.*')
            ]
            filepath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=filetypes
            )

        if filepath:
            try:
                content = text_area.get("1.0", tk.END)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                current_filepath = filepath
                window.title(f'VIX editor - {filepath}')
                messagebox.showinfo("Save", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def on_escape_pressed(event):
        response = messagebox.askyesnocancel(
            "Exit",
            "Do you want to save the changes before exiting?"
        )

        if response is True:
            save_file()
            window.destroy()
        elif response is False:
            window.destroy()

    def undo_action(event=None):
        try:
            text_area.edit_undo()
        except tk.TclError:
            pass

    def redo_action(event=None):
        try:
            text_area.edit_redo()
        except tk.TclError:
            pass
    window.bind('<Escape>', on_escape_pressed)
    window.bind('<Control-z>', undo_action)
    window.bind('<Command-z>', undo_action)

    window.bind('<Control-y>', redo_action)
    window.bind('<Command-y>', redo_action)
    window.bind('<Control-Shift-Z>', redo_action)

    if len(sys.argv) > 1:
        file_to_open = sys.argv[1]
        open_file(file_to_open)

    window.mainloop()

creating()
