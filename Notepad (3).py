import tkinter as tk
from tkinter import filedialog, messagebox, font

class Notepad: # membuat kelas Notepad
    def __init__(self, root):# Inisialisasi Notepad dengan jendela root
        self.root = root  # Menyimpan jendela root sebagai atribut objek Notepad
        self.root.title("Notepad")  # Mengatur judul jendela root menjadi "Notepad"
        self.text_area = tk.Text(self.root)  # Membuat area teks di dalam jendela root
        self.text_area.pack(expand=True, fill='both')  # Menempatkan area teks di dalam jendela 
        self.create_menu()  # Membuat menu pada Notepad


    def create_menu(self):  # Membuat menu-bar dan submenu untuk Notepad
        menu_bar = tk.Menu(self.root)  # Membuat objek menu_bar 
        # Menu File
        file_menu = tk.Menu(menu_bar, tearoff=0)  # Membuat objek file_menu 
        file_menu.add_command(label="New", command=self.new_file)  # Menambahkan opsi menu "New" ke file_menu
        file_menu.add_command(label="Open", command=self.open_file)  # Menambahkan opsi menu "Open" ke file_menu 
        file_menu.add_command(label="Save", command=self.save_file)  # Menambahkan opsi menu "Save" ke file_menu 
        file_menu.add_separator()  # Menambahkan garis pemisah di file_menu
        file_menu.add_command(label="Exit", command=self.exit_app)  # Menambahkan opsi menu "Exit" ke file_menu 
        menu_bar.add_cascade(label="File", menu=file_menu)  # Menambahkan menu "File" ke menu_bar dengan file_menu sebagai submenu

        # Menu Edit
        edit_menu = tk.Menu(menu_bar, tearoff=0)  # Membuat objek edit_menu 
        edit_menu.add_command(label="Cut", command=self.cut_text)  # Menambahkan opsi menu "Cut" ke edit_menu 
        edit_menu.add_command(label="Copy", command=self.copy_text)  # Menambahkan opsi menu "Copy" ke edit_menu 
        edit_menu.add_command(label="Paste", command=self.paste_text)  # Menambahkan opsi menu "Paste" ke edit_menu 
        edit_menu.add_separator()  # Menambahkan garis pemisah di edit_menu
        edit_menu.add_command(label="Bold", command=self.toggle_bold)  # Menambahkan opsi menu "Bold" ke edit_menu 
        edit_menu.add_command(label="Italic", command=self.toggle_italic)  # Menambahkan opsi menu "Italic" ke edit_menu 
        edit_menu.add_command(label="Underline", command=self.toggle_underline)  # Menambahkan opsi menu "Underline" ke edit_menu 
        menu_bar.add_cascade(label="Edit", menu=edit_menu)  # Menambahkan menu "Edit" ke menu_bar dengan edit_menu sebagai submenu


        # Menu Zoom
        zoom_menu = tk.Menu(menu_bar, tearoff=0)  # Membuat objek zoom_menu 
        zoom_menu.add_command(label="Zoom In Font Size", command=self.increase_font_size)  # Menambahkan opsi menu "Zoom In Font Size" ke zoom_menu 
        zoom_menu.add_command(label="Zoom Out Font Size", command=self.decrease_font_size)  # Menambahkan opsi menu "Zoom Out Font Size" ke zoom_menu 
        menu_bar.add_cascade(label="View", menu=zoom_menu)  # Menambahkan menu "View" ke menu_bar 


        self.root.config(menu=menu_bar) # Mengatur menu-bar ke jendela root

    def new_file(self):
        self.text_area.delete(1.0, tk.END) # Menghapus semua teks dalam area teks

    def open_file(self):
        # Membuka file dan menampilkan isinya dalam area teks
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Meminta pengguna untuk memilih file 
        if file_path:  # Jika file_path tidak kosong, artinya pengguna telah memilih file
                try:
                    with open(file_path, 'r') as file:  # Membuka file yang dipilih dalam mode baca ('r') 
                        self.text_area.delete(1.0, tk.END)  # Menghapus semua teks yang ada di area teks sebelumnya
                        self.text_area.insert(tk.END, file.read())  # Memasukkan isi file yang dibuka ke dalam area teks di akhir teks yang ada
                except Exception as e:  # Menangkap kesalahan yang mungkin terjadi saat membuka atau membaca file
                    messagebox.showerror("Error", str(e))  # Menampilkan kotak dialog kesalahan dengan pesan yang menjelaskan kesalahan yang terjadi


    def save_file(self):
        # Menyimpan isi area teks ke dalam file yang ditentukan
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])  # Meminta pengguna untuk memilih lokasi dan nama file 
        if file_path:  # Jika file_path tidak kosong, artinya pengguna telah memilih lokasi dan nama file
                try:
                    with open(file_path, 'w') as file:  # Membuka file yang dipilih dalam mode tulis ('w') 
                        text_content = self.text_area.get(1.0, tk.END)  # Mengambil seluruh teks yang ada di dalam area teks
                        file.write(text_content)  # Menulis teks yang diambil ke dalam file yang dipilih
                except Exception as e:  # Menangkap kesalahan yang mungkin terjadi saat menyimpan file
                     messagebox.showerror("Error", str(e))  # Menampilkan kotak dialog kesalahan dengan pesan yang menjelaskan kesalahan yang terjadi


    def exit_app(self):
        # Menampilkan dialog konfirmasi sebelum keluar dari aplikasi
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def cut_text(self):
        # Memotong teks yang dipilih dalam area teks
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        # Menyalin teks yang dipilih dalam area teks
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        # Menempelkan teks yang disalin dalam area teks
        self.text_area.event_generate("<<Paste>>")

    def toggle_bold(self):
        # Mengubah format teks menjadi tebal atau normal
        current_font_weight = self.text_area['font'].split(' ')[1]
        if current_font_weight == 'normal':
            self.text_area.configure(font=(None, None, 'bold'))
        else:
            self.text_area.configure(font=(None, None, 'normal'))

    def toggle_italic(self):
        # Mengubah format teks menjadi miring atau normal
        current_font_slant = self.text_area['font'].split(' ')[2]
        if current_font_slant == 'roman':
            self.text_area.configure(font=(None, None, 'italic'))
        else:
            self.text_area.configure(font=(None, None, 'roman'))

    def toggle_underline(self):
        # Mengubah format teks menjadi bergaris bawah atau normal
        current_font_underline = 'underline' in self.text_area['font'].split(' ')
        if current_font_underline:
            self.text_area.configure(font=(None, None, 'normal'))
        else:
            self.text_area.configure(font=(None, None, 'underline'))

    def increase_font_size(self):
        # Memperbesar ukuran font teks
        current_font_size = self.text_area['font']
        font_size = font.Font(font=current_font_size).actual()['size']
        new_font_size = font_size + 1
        self.change_font_size(new_font_size)

    def decrease_font_size(self):
        # Memperkecil ukuran font teks
        current_font_size = self.text_area['font']
        font_size = font.Font(font=current_font_size).actual()['size']
        new_font_size = font_size - 1
        if new_font_size > 0:
            self.change_font_size(new_font_size)

    def change_font_size(self, size):
        # Mengubah ukuran font teks
        current_font_family = self.text_area['font']
        font_family = font.Font(font=current_font_family).actual()['family']
        self.text_area.configure(font=(font_family, size))

if __name__ == '__main__':
    # Membuat jendela root untuk Notepad
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
