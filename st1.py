import streamlit as st
from module import DFA
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Menambahkan CSS untuk membuat judul rata tengah
    st.markdown("""
        <style>
        .title {
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Menampilkan judul rata tengah
    st.markdown("<h1 class='title'>Sistem Seleksi 5 Penjaluran Prodi Informatika</h1>", unsafe_allow_html=True)
    st.write('Pilih Penjaluran')

    # Pilihan penjaluran
    penjaluran_options = ['J1', 'J2', 'J3', 'J4', 'J5']
    penjaluran = st.selectbox('', penjaluran_options)

    # Daftar mata kuliah wajib berdasarkan penjaluran
    mata_kuliah_wajib = {
        'J1': ['ALP', 'TBO', 'BD', 'MI', 'SD', 'MD1'],
        'J2': ['ALP', 'RPL', 'BD', 'MI', 'SD', 'DAA'],
        'J3': ['ALP', 'MI', 'BD', 'SDG', 'DAA', 'MD1'],
        'J4': ['ALP', 'SDG', 'BD', 'MI', 'SD', 'SO'],
        'J5': ['ALP', 'KDJK', 'RPL', 'MI', 'MD2', 'SO']
    }
    mata_kuliah_dict = {
        'ALP': 'Algoritma dan Pemrograman',
        'BD': 'Basis Data',
        'DAA': 'Desain dan Analisis Algoritma',
        'IMK': 'Interaksi Manusia dan Komputer',
        'KDJK': 'Komunikasi Data dan Jaringan Komputer',
        'MD1': 'Matematika Diskrit 1',
        'MD2': 'Matematika Diskrit 2',
        'MI': 'Matematika Informatika',
        'PBO': 'Pemrograman Berorientasi Objek',
        'RPL': 'Rekayasa Perangkat Lunak',
        'SD': 'Struktur Data',
        'SDG': 'Sistem Digital',
        'SO': 'Sistem Operasi',
        'TBO': 'Teori Bahasa dan Otomata'
    }
    # Inisialisasi variabel selected_mata_kuliah sebagai list kosong
    selected_mata_kuliah = []
    
    # Mendapatkan daftar mata kuliah wajib berdasarkan penjaluran yang dipilih
    mata_kuliah_wajib_selected = mata_kuliah_wajib.get(penjaluran, [])

    # Menampilkan mata kuliah wajib berdasarkan penjaluran yang dipilih
    for mata_kuliah in mata_kuliah_wajib_selected:
        nama_mata_kuliah = mata_kuliah_dict.get(mata_kuliah, mata_kuliah)
        st.write(f'Input nilai {nama_mata_kuliah}')
        derajat_nilai_options = {
            '1': 'A',
            '2': 'B+',
            '3': 'B',
            '4': 'C',
            '5': 'D',
            '6': 'E'
        }
        derajat_nilai = st.selectbox(f'nilai {nama_mata_kuliah} :', list(derajat_nilai_options.keys()), format_func=lambda x: derajat_nilai_options[x])
        selected_mata_kuliah.append((mata_kuliah, derajat_nilai))

    # Pilihan sertifikat
    sertifikat_options = {
        'Y': 'Ya',
        'T': 'Tidak'
    }
    sertifikat = st.selectbox('Apakah Anda Memiliki Sertifikat Juara Lomba Bidang Teknologi?', list(sertifikat_options.keys()), format_func=lambda x: sertifikat_options[x])

    if st.button('Submit'):
        input_string = f'{penjaluran[1:]}'
        input_string += f'{penjaluran[1:]}'


        for mata_kuliah, nilai in selected_mata_kuliah:
            if penjaluran[1:] == '1':
                if mata_kuliah == 'TBO':
                    if nilai != '1':
                        input_string += f'{nilai}'
                        input_string += f'{sertifikat}'
                        continue
            elif penjaluran[1:] == '2':
                if mata_kuliah == 'RPL':
                    if nilai != '1':
                        input_string += f'{nilai}'
                        input_string += f'{sertifikat}'
                        continue

            elif penjaluran[1:] == '3':
                if mata_kuliah == 'MI':
                    if nilai != '1':
                        input_string += f'{nilai}'
                        input_string += f'{sertifikat}'
                        continue

            elif penjaluran[1:] == '4':
                if mata_kuliah == 'SDG':
                    if nilai != '1':
                        input_string += f'{nilai}'
                        input_string += f'{sertifikat}'
                        continue

            elif penjaluran[1:] == '5':
                if mata_kuliah == 'KDJK':
                    if nilai != '1':
                        input_string += f'{nilai}'
                        input_string += f'{sertifikat}'
                        continue


            input_string += f'{nilai}'
        #input_string += f'{sertifikat}'
        # st.write(input_string)
        # st.write(selected_mata_kuliah)

        a = DFA.dfa()
        a.addFinalState("ACC")
        result = DFA.automata(a, input_string)
        
        st.subheader('Hasil Pengecekan :')
        if result == True:
            st.header(f"Diterima di Penjaluran {penjaluran}")
        elif result == False:
            st.header(f"Ditolak di Penjaluran {penjaluran}")
        else:
            st.header("Input Illegal")

        # Menampilkan tabel nilai yang diinputkan oleh pengguna
        st.subheader('Tabel Nilai')
        table_data = []
        table_data.append(['Jurusan yang Dicek', penjaluran])
        for mata_kuliah, nilai in selected_mata_kuliah:
            nama_mata_kuliah_lengkap = mata_kuliah_dict.get(mata_kuliah, mata_kuliah)
            nilai_huruf = derajat_nilai_options.get(nilai, nilai)
            table_data.append([f'Nilai {nama_mata_kuliah_lengkap}', nilai_huruf])
        table_data.append(['Sertifikat Juara Lomba Bidang Teknologi', 'Ya' if sertifikat == 'Y' else 'Tidak'])
        table_data.append(['Hasil Seleksi', f'Diterima di Penjaluran {penjaluran}' if result else f'Ditolak di Penjaluran {penjaluran}'])

        df = pd.DataFrame(table_data[1:], columns=table_data[0])

        # Menampilkan gambar tabel dengan latar belakang putih
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=['#f2f2f2'] * len(df.columns))
        st.pyplot(fig)

        # Menggunakan matplotlib untuk membuat gambar dari DataFrame
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('off')  # Menyembunyikan sumbu pada gambar
        ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=['#ffffff'] * len(df.columns))
        plt.savefig('tabel.png', bbox_inches='tight', dpi=300)  # Menyimpan gambar dengan resolusi 300 DPI

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

if __name__ == '__main__':
    main()
