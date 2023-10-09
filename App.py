import streamlit as st
import csv

# Step 1: Define Kontak struct
class Kontak:
    def __init__(self, nama, email, telepon):
        self.nama = nama
        self.email = email
        self.telepon = telepon

# Step 2: Load existing data or create an empty list
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

# Step 3: Define functions for each operation
def tambah_kontak():
    nama = st.text_input("Nama:")
    email = st.text_input("Email:")
    telepon = st.text_input("Nomor Telepon:")

    if st.button("Tambah Kontak"):
        kontak_baru = Kontak(nama, email, telepon)
        daftar_kontak.append(kontak_baru)
        save_data(daftar_kontak)
        st.success("Kontak berhasil ditambahkan!")

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

def tampilkan_daftar_kontak():
    st.header("Daftar Kontak")
    for kontak in daftar_kontak:
        st.write(f"Nama: {kontak.nama}")
        st.write(f"Email: {kontak.email}")
        st.write(f"Nomor Telepon: {kontak.telepon}")
        st.write("-" * 20)

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

# Step 4: Main program
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