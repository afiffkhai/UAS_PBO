# UAS_PBO

Pada  Tugas  Akhir  kami  yang  diperuntukkan  UAS  kali  ini,  kami  membuat  Notepad  menggunakan  bahasa  pemrograman  Pyhton  menggunakan  tkinter.  
Notepad  memiliki  beragam  kegunaan  yang  membuatnya  menjadi  salah  satu  aplikasi  yang  penting  dalam  komputasi  sehari-hari.  Dengan  Notepad,  pengguna  dapat  membuat,  mengedit,  dan  menyimpan  catatan  teks  sederhana,  memo,  atau  daftar  tugas  yang  penting.  Selain  itu,  Notepad  juga  dapat  digunakan  untuk  menulis  dan  mengedit  kode  sederhana  dalam  bahasa  pemrograman,  melakukan  pengeditan  cepat  pada  file  konfigurasi,  menyimpan  catatan  penting  secara  sementara,  menyalin  dan  menempelkan  teks  tanpa  format,  serta  membaca  dan  memodifikasi  file  teks  biasa  dengan  mudah.  Kemudahan  penggunaan  dan  kesederhanaan  Notepad  menjadikannya  alat  yang  serbaguna  dan  praktis  untuk  penggunaan  sehari-hari.
Kami  akan  menjelaskan  secara  singkat  penjelasan  koding  yang  telah  kami  buat.  Berikut  penjelasannya  :  
import tkinter as tk
from tkinter import filedialog, messagebox, font

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')
        self.create_menu()

Pertama ada `import tkinter as tk`: Baris ini mengimpor modul Tkinter dan memberikan alias `tk` ke modul tersebut. Tkinter digunakan untuk membuat antarmuka grafis (GUI) pada Python. dan`from tkinter import filedialog, messagebox, font`: Baris ini mengimpor beberapa kelas dan fungsi dari modul Tkinter yang akan digunakan, yaitu `filedialog`, `messagebox`, dan `font`.
Lalu  konstruktor  init,  kita  menginisialisasi  jendela  utama  (root)  menggunakan  root  yang  diterima  sebagai  argumen.  Kemudian,  kita  memberi  judul  pada  jendela  utama  menggunakan  self.root.title("Notepad").  Selanjutnya,  kita  membuat  area  teks  menggunakan  tk.Text(self.root)  dan  mengaturnya  agar  mengisi  seluruh  ruang  yang  tersedia  menggunakan  .pack(expand=True,  fill='both').  Terakhir,  kita  memanggil  metode  create_menu()  untuk  membuat  menu.
def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # Menu File
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)


Selanjutnya create_menu()  dalam  kelas  Notepad.  Di  dalam  metode  ini,  kita  membuat  beberapa  menu  pada  menu-bar  yang  akan  ditampilkan  di  aplikasi  Notepad.Objek  menu-file  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).Kemudian,  kita  menambahkan  opsi-opsi  seperti  "New"  ,  "Open"  ,"Save"  ,dan  "Exit"menggunakan.add_command().menu_bar.add_cascade(label="File",menu=file_menu)  digunakan  untuk  menambahkan  menu-file  ke  dalam  menu-bar.Objekmenu-edit  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).
 # Menu Edit
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Bold", command=self.toggle_bold)
        edit_menu.add_command(label="Italic", command=self.toggle_italic)
        edit_menu.add_command(label="Underline", command=self.toggle_underline)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
Kemudian,  kita  menambahkan  opsi-opsi  seperti  "Cut",  "Copy",  dan  "Paste"  menggunakan  .add_command().  menu_bar.add_cascade(label="Edit",  menu=edit_menu)  digunakan  untuk  menambahkan  menu-edit  ke  dalam  menu-bar.Objek  
 # Menu Zoom
        zoom_menu = tk.Menu(menu_bar, tearoff=0)
        zoom_menu.add_command(label="Zoom In Font Size", command=self.increase_font_size)
        zoom_menu.add_command(label="Zoom Out Font Size", command=self.decrease_font_size)
        menu_bar.add_cascade(label="View", menu=zoom_menu)

        self.root.config(menu=menu_bar)
menu-zoom  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).Kemudian,  kita  menambahkan  opsi-opsi  seperti  "Increase  Font  Size"  dan  "Decrease  Font  Size"  menggunakan  .add_command().menu_bar.add_cascade(label="Zoom",  menu=zoom_menu)  digunakan  untuk  menambahkan  menu-zoom  ke  dalam  menu-bar.Terakhir,  kita  mengatur  menu-bar  yang  telah  dibuat  pada  jendela  utama  menggunakan  self.root.config(menu=menu_bar).  Dengan  demikian,  menu-bar  akan  ditampilkan  di  aplikasi  Notepad.
 def new_file(self):
        # Menghapus semua teks dalam area teks
        self.text_area.delete(1.0, tk.END)
Selanjutnya lagi metode  new_file(self):  Metode  ini  digunakan  untuk  membuat  file  baru  dengan  menghapus  seluruh  teks  yang  ada  di  dalam  text_area.  Ini  dilakukan  dengan  menggunakan  self.text_area.delete(1.0,  tk.END)  yang  menghapus  teks  dari  baris  1,  kolom  0  hingga  akhir  teks. 
def open_file(self):
        # Membuka file dan menampilkan isinya dalam area teks
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", str(e))
 Metode  open_file(self):  Metode  ini  digunakan  untuk  membuka  file  yang  ada  dengan  menggunakan  dialog  pemilihan  file  menggunakan  filedialog.askopenfilename().  Jika  file  berhasil  dipilih,  maka  metode  ini  akan  membaca  konten  file  tersebut  menggunakan  open(file_path,  'r')  dan  menghapus  teks  yang  ada  di  text_area.  Selanjutnya,  konten  file  akan  dimasukkan  ke  dalam  text_area  menggunakan  self.text_area.insert(tk.END,  file.read()). 
 def save_file(self):
        # Menyimpan isi area teks ke dalam file yang ditentukan
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    text_content = self.text_area.get(1.0, tk.END)
                    file.write(text_content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

 Metode  save_file(self):  Metode  ini  digunakan  untuk  menyimpan  konten  text_area  ke  dalam  file  yang  dipilih  menggunakan  dialog  penyimpanan  file  menggunakan  filedialog.asksaveasfilename().  Jika  file  berhasil  dipilih,  maka  metode  ini  akan  membuka  file  tersebut  untuk  penulisan  menggunakan  open(file_path,  'w').  Kemudian,  konten  text_area  akan  diambil  menggunakan  self.text_area.get(1.0,  tk.END)  dan  ditulis  ke  dalam  file  menggunakan  file.write(text_content).  
  def exit_app(self):
        # Menampilkan dialog konfirmasi sebelum keluar dari aplikasi
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()
Metode  exit_app(self):  Metode  ini  digunakan  untuk  keluar  dari  aplikasi  dengan  menghancurkan  jendela  utama  menggunakan  self.root.destroy().  Sebelum  keluar,  metode  ini  akan  menampilkan  dialog  konfirmasi  menggunakan  messagebox.askokcancel()  dengan  pesan  "Are  you  sure  you  want  to  quit?".  Jika  pengguna  memilih  "OK",  maka  jendela  utama  akan  dihancurkan
Pada  kode  exit_app(self):  Metode  ini  digunakan  untuk  menutup  aplikasi  notepad.  Ketika  metode  ini  dipanggil,  ia  akan  menampilkan  kotak  dialog  konfirmasi  "Are  you  sure  you  want  to  quit?"  menggunakan  messagebox.askokcancel.  Jika  pengguna  menekan  tombol  "OK",  maka  self.root.destroy()  akan  dipanggil  untuk  menutup  jendela  notepad.  
 def cut_text(self):
        # Memotong teks yang dipilih dalam area teks
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        # Menyalin teks yang dipilih dalam area teks
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        # Menempelkan teks yang disalin dalam area teks
        self.text_area.event_generate("<<Paste>>")

cut_text(self):  Metode  ini  menghasilkan  peristiwa  "Cut"  pada  text_area.  Dengan  demikian,  teks  yang  dipilih  dalam  text_area  akan  dipotong  ke  clipboard.  copy_text(self):  Metode  ini  menghasilkan  peristiwa  "Copy"  pada  text_area.  Ini  akan  menyalin  teks  yang  dipilih  dalam  text_area  ke  clipboard.  paste_text(self):  Metode  ini  menghasilkan  peristiwa  "Paste"  pada  text_area.  Ini  akan  mengambil  teks  dari  clipboard  dan  memasukkannya  ke  text_area  pada  posisi  kursor  saat  ini. 
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
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
 increase_font_size(self):  Metode  ini  digunakan  untuk  meningkatkan  ukuran  font  dalam  text_area.  Itu  mengambil  ukuran  font  saat  ini  dari  text_area,  menambahkannya  dengan  1,  dan  kemudian  memanggil  metode  change_font_size  dengan  ukuran  font  yang  baru.  decrease_font_size(self):  Metode  ini  digunakan  untuk  mengurangi  ukuran  font  dalam  text_area.  Ini  mirip  dengan  increase_font_size,  tetapi  mengurangi  ukuran  font  dengan  1  dan  memeriksa  agar  ukuran  font  tidak  menjadi  negatif  sebelum  memanggil  change_font_size.  change_font_size(self,  size):  Metode  ini  mengubah  ukuran  font  dalam  text_area  menjadi  ukuran  yang  diberikan.  Itu  mengambil  keluarga  font  saat  ini  dari  text_area  dan  kemudian  mengonfigurasi  text_area  dengan  font  yang  baru,  yang  menggunakan  ukuran  yang  diberikan  tetapi  keluarga  font  yang  sama.
Kode  if  name  ==  'main':  merupakan  konvensi  dalam  Python  yang  menjalankan  blok  kode  yang  berada  di  dalamnya  hanya  jika  file  tersebut  dijalankan  langsung  sebagai  program  utama.  root  =  tk.Tk():  Baris  ini  membuat  objek  Tkinter  baru  dengan  menyimpannya  dalam  variabel  root.  Objek  Tkinter  ini  merupakan  jendela  utama  aplikasi  yang  akan  menampung  elemen-elemen  GUI  yang  akan  ditampilkan.  notepad  =  Notepad(root)  Pada  baris  ini,  objek  Notepad  dibuat  dengan  memberikan  root  sebagai  argumen  konstruktor.  Dengan  melakukan  ini,  objek  Notepad  akan  memiliki  akses  ke  jendela  utama  root  dan  dapat  menambahkan  elemen-elemen  GUI  ke  dalamnya.  root.mainloop()  Metode  mainloop()  adalah  metode  utama  dalam  aplikasi  Tkinter.  Ini  akan  menjalankan  loop  utama  yang  akan  merespons  input  pengguna,  memperbarui  tampilan,  dan  mempertahankan  aplikasi  tetap  berjalan  sampai  jendela  ditutup.  Jadi,  dengan  memanggil  root.mainloop(),  aplikasi  Tkinter  akan  dimulai  dan  berjalan  secara  terus-menerus  sampai  jendela  ditutup.
Kodingan di atas adalah sebuah program sederhana yang menggunakan modul Tkinter dalam bahasa pemrograman Python untuk membuat aplikasi Notepad. Aplikasi ini memiliki fungsi dasar seperti membuat file baru, membuka file yang ada, menyimpan file, mengedit teks (memotong, menyalin, dan menempel), dan mengubah ukuran font
