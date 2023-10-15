import streamlit as st
import csv
import pandas as pd

# 1. Buatlah sebuah tipe data terstruktur (struct) yang disebut Kontak yang memiliki atribut-atribut berikut:
# Nama kontak (string)
# Alamat email kontak (string)
# No telepon kontak (string)

class Kontak:
    def __init__(self, nama, email, telepon):
        self.nama = nama
        self.email = email
        self.telepon = telepon

# 2. array untuk menyimpan kontak-kontak
def load_data():
    try:
        with open('kontak.csv', mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return [Kontak(*row) for row in data]
    except FileNotFoundError:
        return []

def save_data(daftar_kontak):
    with open('kontak.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for kontak in daftar_kontak:
            writer.writerow([kontak.nama, kontak.email, kontak.telepon])

# 3. Fungsi tambah_kontak yang memungkinkan pengguna untuk memasukkan data kontak baru ke dalam program.
def tambah_kontak():
    nama = st.text_input("Nama:")
    email = st.text_input("Email:")
    telepon = st.text_input("Nomor Telepon:")

    if st.button("Tambah Kontak"):
        kontak_baru = Kontak(nama, email, telepon)
        daftar_kontak.append(kontak_baru)
        save_data(daftar_kontak)
        st.success("Kontak berhasil ditambahkan!")

# 4. Fungsi hapus_kontak yang memungkinkan pengguna untuk menghapus kontak berdasarkan nama kontak.
def hapus_kontak():
    nama_hapus = st.text_input("Nama Kontak yang akan dihapus:")
    if st.button("Hapus Kontak"):
        for kontak in daftar_kontak:
            if kontak.nama.lower() == nama_hapus.lower():
                daftar_kontak.remove(kontak)
                save_data(daftar_kontak)
                st.success(f"Kontak {kontak.nama} berhasil dihapus!")
                break
        else:
            st.warning(f"Tidak ada kontak dengan nama {nama_hapus}.")

# 6. Fungsi tampilkan_daftar_kontak yang menampilkan daftar semua kontak yang ada, termasuk nama, nomor telepon, dan alamat email.
def tampilkan_daftar_kontak():
    st.header("Daftar Kontak")
    data = [[i+1] + [kontak.nama, kontak.email, kontak.telepon] for i, kontak in enumerate(daftar_kontak)]
    if data:
        df = pd.DataFrame(data, columns=["No", "Nama", "Email", "Nomor Telepon"])
        df = df.set_index("No")  # Menjadikan kolom "No" sebagai indeks
        st.table(df)
    else:
        st.write("Tidak ada kontak yang tersedia.")

# 7. Fungsi cari_kontak yang memungkinkan pengguna untuk mencari kontak berdasarkan nama.
def cari_kontak():
    nama_cari = st.text_input("Cari Nama Kontak:")
    if st.button("Cari Kontak"):
        ditemukan = False
        for kontak in daftar_kontak:
            if kontak.nama.lower() == nama_cari.lower():
                st.header("Kontak Ditemukan:")
                st.write(f"Nama: {kontak.nama}")
                st.write(f"Email: {kontak.email}")
                st.write(f"Nomor Telepon: {kontak.telepon}")
                ditemukan = True
                break
        if not ditemukan:
            st.warning(f"Tidak ada kontak dengan nama {nama_cari}.")

# 7. Program utama yang memberikan menu kepada pengguna untuk melakukan operasi-operasi yang telah dibuat.
def main():
    st.title("Aplikasi Pengelola Kontak")
    
    menu = st.sidebar.selectbox("Menu:", ["Tambah Kontak", "Hapus Kontak", "Tampilkan Daftar Kontak", "Cari Kontak"])
    
    if menu == "Tambah Kontak":
        tambah_kontak()
    elif menu == "Hapus Kontak":
        hapus_kontak()
    elif menu == "Tampilkan Daftar Kontak":
        tampilkan_daftar_kontak()
    elif menu == "Cari Kontak":
        cari_kontak()

if __name__ == "__main__":
    daftar_kontak = load_data()
    main()