import time
import matplotlib.pyplot as plt

library = [
    {"title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005},
    {"title": "Sang Pemimpi", "author": "Andrea Hirata", "year": 2006},
    {"title": "Edensor", "author": "Andrea Hirata", "year": 2007},
    {"title": "Maryamah Karpov", "author": "Andrea Hirata", "year": 2009},
    {"title": "Pulang", "author": "Tere Liye", "year": 2017},
    {"title": "Hujan", "author": "Tere Liye", "year": 2016},
    {"title": "Bulan", "author": "Tere Liye", "year": 2017},
    {"title": "Daun Yang Jatuh Tak Pernah Membenci Angin", "author": "Tere Liye", "year": 2010},
    {"title": "Tenggelamnya Kapal Van Der Wijck", "author": "Haji Abdul Malik Karim Amrullah", "year": 1939},
    {"title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "year": 1980},
    {"title": "Anak Semua Bangsa", "author": "Pramoedya Ananta Toer", "year": 1981},
    {"title": "Jejak Langkah", "author": "Pramoedya Ananta Toer", "year": 1985},
    {"title": "Rumah Kaca", "author": "Pramoedya Ananta Toer", "year": 2000},
    {"title": "Manusia Setengah Salmon", "author": "Raditya Dika", "year": 2011},
    {"title": "Koala Kumal", "author": "Raditya Dika", "year": 2012},
    {"title": "Kambing Jantan", "author": "Raditya Dika", "year": 2005},
    {"title": "Cinta Brontosaurus", "author": "Raditya Dika", "year": 2006},
    {"title": "Rindu", "author": "Tere Liye", "year": 2018},
    {"title": "Matahari", "author": "Tere Liye", "year": 2018},
    {"title": "Hanya Kita", "author": "Tere Liye", "year": 2020},
    {"title": "Bintang", "author": "Tere Liye", "year": 2022},
    {"title": "Garis Waktu", "author": "Fiersa Besari", "year": 2019},
    {"title": "Cinta Tak Pernah Tepat Waktu", "author": "Fiersa Besari", "year": 2017},
    {"title": "Bersama Bintang", "author": "Fiersa Besari", "year": 2020},
    {"title": "Bumi", "author": "Tere Liye", "year": 2014},
    {"title": "Cinta dalam Gelas", "author": "Andrea Hirata", "year": 2010},
    {"title": "Pukul 2 Siang", "author": "Chandra Noor", "year": 2015},
    {"title": "Ayat-Ayat Cinta", "author": "Habiburrahman El Shirazy", "year": 2004},
    {"title": "Ketika Cinta Bertasbih", "author": "Habiburrahman El Shirazy", "year": 2007},
    {"title": "Di Atas Reruntuhan Cinta", "author": "Habiburrahman El Shirazy", "year": 2012},
    {"title": "Perahu Kertas", "author": "Dewi Lestari", "year": 2009},
    {"title": "Supernova: Ksatria, Puteri, dan Bintang Jatuh", "author": "Dewi Lestari", "year": 2002},
    {"title": "Filosofi Kopi", "author": "Dee Lestari", "year": 1995},
    {"title": "Supernova: Akar", "author": "Dewi Lestari", "year": 2009},
    {"title": "Belajar Mencintai", "author": "Tere Liye", "year": 2020},
    {"title": "Gantung", "author": "Tere Liye", "year": 2021},
    {"title": "Emak", "author": "Tere Liye", "year": 2019},
    {"title": "Pulang", "author": "Tere Liye", "year": 2017},
    {"title": "Menyelami Cinta", "author": "Tere Liye", "year": 2019},
    {"title": "Bukan Cinta Biasa", "author": "Yosef Leon", "year": 2020},
    {"title": "Karma", "author": "Fiersa Besari", "year": 2016},
    {"title": "Perjalanan Cinta", "author": "Yosef Leon", "year": 2017},
    {"title": "Rindu Cinta", "author": "Yosef Leon", "year": 2019},
    {"title": "Cinta Tak Pernah Tersisa", "author": "Dina Nadhirah", "year": 2018},
    {"title": "Luka dalam Cinta", "author": "Dina Nadhirah", "year": 2019},
    {"title": "Melodi Cinta", "author": "Fiersa Besari", "year": 2018},
    {"title": "Cinta dan Cerita", "author": "Fiersa Besari", "year": 2020},
    {"title": "Jalan Cinta", "author": "Yosef Leon", "year": 2021},
    {"title": "Hidup itu Indah", "author": "Tere Liye", "year": 2015},
    {"title": "Pintu Cinta", "author": "Yosef Leon", "year": 2018},
    {"title": "Cinta Sejati", "author": "Yosef Leon", "year": 2017},
    {"title": "Rindu Tak Tertahankan", "author": "Tere Liye", "year": 2018},
    {"title": "Antologi Cinta", "author": "Tere Liye", "year": 2017},
    {"title": "Kisah Cinta di Musim Salju", "author": "Mira W", "year": 2019},
    {"title": "Dari Hati", "author": "Fiersa Besari", "year": 2020},
    {"title": "Cinta Tak Pernah Tepat Waktu", "author": "Fiersa Besari", "year": 2017},
    {"title": "Senja di Peluk Hujan", "author": "Fiersa Besari", "year": 2021},
    {"title": "Sekali Lagi", "author": "Mira W", "year": 2020},
    {"title": "Kau, Aku, dan Cinta", "author": "Mira W", "year": 2021},
    {"title": "Rindu di Langit Biru", "author": "Fiersa Besari", "year": 2020},
    {"title": "Saling Menjaga", "author": "Fiersa Besari", "year": 2019},
    {"title": "Mencintai Cinta", "author": "Mira W", "year": 2021},
    {"title": "Cinta Punya Cerita", "author": "Yosef Leon", "year": 2020},
    {"title": "Ketika Rindu Menyapa", "author": "Yosef Leon", "year": 2021},
    {"title": "Cinta di Ujung Dunia", "author": "Yosef Leon", "year": 2020},
    {"title": "Menyusuri Cinta", "author": "Yosef Leon", "year": 2020},
    {"title": "Di Tepi Lautan Cinta", "author": "Yosef Leon", "year": 2021},
    {"title": "Menanti Cinta", "author": "Mira W", "year": 2021},
    {"title": "Hati yang Luka", "author": "Tere Liye", "year": 2017},
    {"title": "Mendekap Cinta", "author": "Mira W", "year": 2020},
    {"title": "Bersama Cinta", "author": "Mira W", "year": 2021},
    {"title": "Menahan Rindu", "author": "Fiersa Besari", "year": 2020},
    {"title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005},
    {"title": "Sang Pemimpi", "author": "Andrea Hirata", "year": 2006},
    {"title": "Edensor", "author": "Andrea Hirata", "year": 2007},
    {"title": "Maryamah Karpov", "author": "Andrea Hirata", "year": 2009},
    {"title": "Pulang", "author": "Tere Liye", "year": 2017},
    {"title": "Hujan", "author": "Tere Liye", "year": 2016},
    {"title": "Bulan", "author": "Tere Liye", "year": 2017},
    {"title": "Daun Yang Jatuh Tak Pernah Membenci Angin", "author": "Tere Liye", "year": 2010},
    {"title": "Tenggelamnya Kapal Van Der Wijck", "author": "Haji Abdul Malik Karim Amrullah", "year": 1939},
    {"title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "year": 1980},
    {"title": "Anak Semua Bangsa", "author": "Pramoedya Ananta Toer", "year": 1981},
    {"title": "Jejak Langkah", "author": "Pramoedya Ananta Toer", "year": 1985},
    {"title": "Rumah Kaca", "author": "Pramoedya Ananta Toer", "year": 2000},
    {"title": "Manusia Setengah Salmon", "author": "Raditya Dika", "year": 2011},
    {"title": "Koala Kumal", "author": "Raditya Dika", "year": 2012},
    {"title": "Kambing Jantan", "author": "Raditya Dika", "year": 2005},
    {"title": "Cinta Brontosaurus", "author": "Raditya Dika", "year": 2006},
    {"title": "Rindu", "author": "Tere Liye", "year": 2018},
    {"title": "Matahari", "author": "Tere Liye", "year": 2018},
    {"title": "Hanya Kita", "author": "Tere Liye", "year": 2020},
    {"title": "Bintang", "author": "Tere Liye", "year": 2022},
    {"title": "Garis Waktu", "author": "Fiersa Besari", "year": 2019},
    {"title": "Cinta Tak Pernah Tepat Waktu", "author": "Fiersa Besari", "year": 2017},
    {"title": "Bersama Bintang", "author": "Fiersa Besari", "year": 2020},
    {"title": "Bumi", "author": "Tere Liye", "year": 2014},
    {"title": "Cinta dalam Gelas", "author": "Andrea Hirata", "year": 2010},
    {"title": "Pukul 2 Siang", "author": "Chandra Noor", "year": 2015},
    {"title": "Ayat-Ayat Cinta", "author": "Habiburrahman El Shirazy", "year": 2004},
    {"title": "Ketika Cinta Bertasbih", "author": "Habiburrahman El Shirazy", "year": 2007},
    {"title": "Di Atas Reruntuhan Cinta", "author": "Habiburrahman El Shirazy", "year": 2012},
    {"title": "Perahu Kertas", "author": "Dewi Lestari", "year": 2009},
    {"title": "Supernova: Ksatria, Puteri, dan Bintang Jatuh", "author": "Dewi Lestari", "year": 2002},
    {"title": "Filosofi Kopi", "author": "Dee Lestari", "year": 1995},
    {"title": "Supernova: Akar", "author": "Dewi Lestari", "year": 2009},
    {"title": "Belajar Mencintai", "author": "Tere Liye", "year": 2020},
    {"title": "Gantung", "author": "Tere Liye", "year": 2021},
    {"title": "Emak", "author": "Tere Liye", "year": 2019},
    {"title": "Pulang", "author": "Tere Liye", "year": 2017},
    {"title": "Menyelami Cinta", "author": "Tere Liye", "year": 2019},
    {"title": "Bukan Cinta Biasa", "author": "Yosef Leon", "year": 2020},
    {"title": "Karma", "author": "Fiersa Besari", "year": 2016},
    {"title": "Perjalanan Cinta", "author": "Yosef Leon", "year": 2017},
    {"title": "Rindu Cinta", "author": "Yosef Leon", "year": 2019},
    {"title": "Cinta Tak Pernah Tersisa", "author": "Dina Nadhirah", "year": 2018},
    {"title": "Luka dalam Cinta", "author": "Dina Nadhirah", "year": 2019},
    {"title": "Melodi Cinta", "author": "Fiersa Besari", "year": 2018},
    {"title": "Cinta dan Cerita", "author": "Fiersa Besari", "year": 2020},
    {"title": "Jalan Cinta", "author": "Yosef Leon", "year": 2021},
    {"title": "Hidup itu Indah", "author": "Tere Liye", "year": 2015},
    {"title": "Pintu Cinta", "author": "Yosef Leon", "year": 2018},
    {"title": "Cinta Sejati", "author": "Yosef Leon", "year": 2017},
    {"title": "Rindu Tak Tertahankan", "author": "Tere Liye", "year": 2018},
    {"title": "Antologi Cinta", "author": "Tere Liye", "year": 2017},
    {"title": "Kisah Cinta di Musim Salju", "author": "Mira W", "year": 2019},
    {"title": "Dari Hati", "author": "Fiersa Besari", "year": 2020},
    {"title": "Cinta Tak Pernah Tepat Waktu", "author": "Fiersa Besari", "year": 2017},
    {"title": "Senja di Peluk Hujan", "author": "Fiersa Besari", "year": 2021},
    {"title": "Sekali Lagi", "author": "Mira W", "year": 2020},
    {"title": "Kau, Aku, dan Cinta", "author": "Mira W", "year": 2021},
    {"title": "Rindu di Langit Biru", "author": "Fiersa Besari", "year": 2020},
    {"title": "Saling Menjaga", "author": "Fiersa Besari", "year": 2019},
    {"title": "Mencintai Cinta", "author": "Mira W", "year": 2021},
    {"title": "Cinta Punya Cerita", "author": "Yosef Leon", "year": 2020},
    {"title": "Ketika Rindu Menyapa", "author": "Yosef Leon", "year": 2021},
    {"title": "Cinta di Ujung Dunia", "author": "Yosef Leon", "year": 2020},
    {"title": "Menyusuri Cinta", "author": "Yosef Leon", "year": 2020},
    {"title": "Di Tepi Lautan Cinta", "author": "Yosef Leon", "year": 2021},
    {"title": "Menanti Cinta", "author": "Mira W", "year": 2021},
    {"title": "Hati yang Luka", "author": "Tere Liye", "year": 2017},
    {"title": "Mendekap Cinta", "author": "Mira W", "year": 2020},
    {"title": "Bersama Cinta", "author": "Mira W", "year": 2021},
    {"title": "Menahan Rindu", "author": "Fiersa Besari", "year": 2020},
     {"title": "Cinta di Ujung Dunia", "author": "Fiersa Besari", "year": 2022},
    {"title": "Jangan Takut Cinta", "author": "Dewi Lestari", "year": 2004},
    {"title": "Pulang Sebelum Awan", "author": "Rintik Sedu", "year": 2019},
    {"title": "Bintang di Langit Kita", "author": "Siti Fatonah", "year": 2018},
    {"title": "Jaga Cintaku", "author": "Andra", "year": 2020},
    {"title": "Luka Tak Terobati", "author": "Tere Liye", "year": 2021},
    {"title": "Bintang Yang Hilang", "author": "Anggi Wijaya", "year": 2019},
    {"title": "Kehidupan Cinta", "author": "Fiersa Besari", "year": 2022},
    {"title": "Mencari Cinta Sejati", "author": "Alya Kurnia", "year": 2017},
    {"title": "Mencintaimu Sampai Mati", "author": "Rama F. A.", "year": 2016},
    {"title": "Cinta dalam Diam", "author": "Dian Agustina", "year": 2020},
    {"title": "Sajak Cinta", "author": "Faisal Aswan", "year": 2019},
    {"title": "Kasih Tak Sampai", "author": "Muhammad Abdurrahman", "year": 2018},
    {"title": "Cinta Mengajar", "author": "Jamilah Zulfikar", "year": 2017},
    {"title": "Rindu Tak Bisa Dilupa", "author": "Rahmat Suryadi", "year": 2018},
    {"title": "Di Balik Cinta", "author": "Vera Sulaiman", "year": 2019},
    {"title": "Selalu Ada Cinta", "author": "Nadia Rasdian", "year": 2020},
    {"title": "Garis Takdir Cinta", "author": "Febri H. F.", "year": 2020},
    {"title": "Dari Hati ke Hati", "author": "Yohana Pratiwi", "year": 2019},
    {"title": "Layar Cinta", "author": "Aliya Fajri", "year": 2021},
    {"title": "Senja dalam Cinta", "author": "Ema Azura", "year": 2022},
    {"title": "Berlindung dalam Cinta", "author": "Pramudya A.", "year": 2020},
    {"title": "Dihantui Cinta", "author": "Cynthia Dwi", "year": 2021},
    {"title": "Mendalami Cinta", "author": "Hani Fikri", "year": 2020},
    {"title": "Berlayar dalam Cinta", "author": "Rania Azmita", "year": 2021},
    {"title": "Dosa Cinta", "author": "Rania Firdya", "year": 2020},
    {"title": "Cinta dalam Cakrawala", "author": "Yusuf Saleh", "year": 2021},
    {"title": "Cinta Menghantui", "author": "Indah Dian", "year": 2019},
    {"title": "Rindu yang Tertinggal", "author": "Tanya Siska", "year": 2021},
    {"title": "Kehilangan Cinta", "author": "Sarah Rizky", "year": 2022},
    {"title": "Penuh Cinta", "author": "Hafizh Alfarezi", "year": 2020},
    {"title": "Cinta Yang Tersisa", "author": "Nabila Syariah", "year": 2020},
    {"title": "Sebuah Cinta", "author": "Rizki Anggi", "year": 2021},
    {"title": "Rindu Dalam Cinta", "author": "Siti Khodijah", "year": 2022},
    {"title": "Jangan Menunggu Cinta", "author": "Hesti Suryani", "year": 2022},
    {"title": "Sekali Cinta", "author": "Rahma Nur", "year": 2021},
    {"title": "Mencari Jalan Cinta", "author": "Kiran Rista", "year": 2022},
    {"title": "Cinta yang Kembali", "author": "Rina Prameswari", "year": 2020},
    {"title": "Selalu Ada Rindu", "author": "Anisa Tanjung", "year": 2021},
    {"title": "Sisa Cinta", "author": "Farah Vindi", "year": 2022},
    {"title": "Menangis dalam Cinta", "author": "Fahira Usman", "year": 2021},
    {"title": "Cinta yang Hilang", "author": "Sani Rahmawati", "year": 2020},
    {"title": "Menyatukan Cinta", "author": "Lutfi Aulia", "year": 2021},
    {"title": "Pernah Cinta", "author": "Rosa Kairun", "year": 2022},
    {"title": "Cinta yang Tidak Terungkap", "author": "Widyawati T.", "year": 2021},
    {"title": "Kehadiran Cinta", "author": "Siti Aisyah", "year": 2021},
    {"title": "Bersama Dalam Cinta", "author": "Amirah Mahira", "year": 2022},
    {"title": "Mengenang Cinta", "author": "Aviiana", "year": 2022},
    {"title": "Cinta di Seberang Laut", "author": "Yasmin Dahlia", "year": 2022},
    {"title": "Menjemput Cinta", "author": "Ayu Kurnia", "year": 2021},
    
    
]
# Fungsi untuk mengurutkan library
def sort_library(library, key):
    return sorted(library, key=lambda x: x[key])

# Fungsi Binary Search Rekursif
def binary_search_recursive(library, left, right, key, value):
    if left > right:
        return []  # Tidak ditemukan

    mid = (left + right) // 2
    mid_value = library[mid][key]

    # Case-insensitive untuk string
    if isinstance(mid_value, str) and isinstance(value, str):
        mid_value = mid_value.lower()
        value = value.lower()

    if mid_value == value:
        # Mencari semua entri dengan atribut yang sama
        results = [library[mid]]
        # Periksa ke kiri
        results.extend(binary_search_recursive(library, left, mid - 1, key, value))
        # Periksa ke kanan
        results.extend(binary_search_recursive(library, mid + 1, right, key, value))
        return results
    elif mid_value < value:
        return binary_search_recursive(library, mid + 1, right, key, value)
    else:
        return binary_search_recursive(library, left, mid - 1, key, value)

# Fungsi Binary Search Iteratif
def binary_search_iterative(library, left, right, key, value):
    results = []
    while left <= right:
        mid = (left + right) // 2
        mid_value = library[mid][key]

        # Case-insensitive untuk string
        if isinstance(mid_value, str) and isinstance(value, str):
            mid_value = mid_value.lower()
            value = value.lower()

        if mid_value == value:
            # Tambahkan elemen yang ditemukan
            results.append(library[mid])

            # Periksa ke kiri
            i = mid - 1
            while i >= 0 and library[i][key] == mid_value:
                results.append(library[i])
                i -= 1

            # Periksa ke kanan
            j = mid + 1
            while j < len(library) and library[j][key] == mid_value:
                results.append(library[j])
                j += 1
            break
        elif mid_value < value:
            left = mid + 1
        else:
            right = mid - 1

    return results

# Fungsi Utama
def main():
    execution_times_recursive = []
    execution_times_iterative = []

    while True:
        print("\nPilih atribut pencarian: 1. Judul, 2. Penulis, 3. Tahun Terbit")
        try:
            choice = int(input("Masukkan pilihan (1/2/3): "))
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.")
            continue

        if choice == 1:
            key = "title"
            value = input("Masukkan judul buku: ")
        elif choice == 2:
            key = "author"
            value = input("Masukkan nama penulis: ")
        elif choice == 3:
            key = "year"
            try:
                value = int(input("Masukkan tahun terbit: "))
            except ValueError:
                print("Tahun harus berupa angka.")
                continue
        else:
            print("Pilihan tidak valid.")
            continue

        # Urutkan library berdasarkan key
        sorted_library = sort_library(library, key)

        # Binary Search Rekursif
        start_time = time.perf_counter()  # Menggunakan perf_counter untuk presisi tinggi
        result_recursive = binary_search_recursive(sorted_library, 0, len(sorted_library) - 1, key, value)
        elapsed_time_recursive = time.perf_counter() - start_time

        # Simpan waktu pencarian rekursif
        execution_times_recursive.append(elapsed_time_recursive)

        # Binary Search Iteratif
        start_time = time.perf_counter()  # Menggunakan perf_counter untuk presisi tinggi
        result_iterative = binary_search_iterative(sorted_library, 0, len(sorted_library) - 1, key, value)
        elapsed_time_iterative = time.perf_counter() - start_time

        # Simpan waktu pencarian iteratif
        execution_times_iterative.append(elapsed_time_iterative)

        # Menampilkan hasil rekursif
        if result_recursive:
            print(f"\n[Rekursif] Buku ditemukan ({len(result_recursive)} hasil):")
            for book in result_recursive:
                print(f" - {book['title']} oleh {book['author']} ({book['year']})")
        else:
            print("\n[Rekursif] Buku tidak ditemukan.")

        # Menampilkan hasil iteratif
        if result_iterative:
            print(f"\n[Iteratif] Buku ditemukan ({len(result_iterative)} hasil):")
            for book in result_iterative:
                print(f" - {book['title']} oleh {book['author']} ({book['year']})")
        else:
            print("\n[Iteratif] Buku tidak ditemukan.")

        # Menampilkan waktu eksekusi
        print(f"\nWaktu pencarian rekursif: {elapsed_time_recursive:.6f} detik")
        print(f"Waktu pencarian iteratif: {elapsed_time_iterative:.6f} detik")

        # Opsi melanjutkan
        cont = input("\nApakah Anda ingin mencari lagi? (y/n): ").lower()
        if cont != 'y':
            print("Terima kasih telah menggunakan program ini.")
            break

    # Menampilkan grafik
    plt.plot(execution_times_recursive, label='Rekursif', marker='o')
    plt.plot(execution_times_iterative, label='Iteratif', marker='o')
    plt.title('Waktu Eksekusi Pencarian')
    plt.xlabel('Pencarian ke-')
    plt.ylabel('Waktu (detik)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Menjalankan program utama
main()