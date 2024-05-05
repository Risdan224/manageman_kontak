"Program Manajemen Kontak"

kontak1 = {'nama' : "Andi", 'HP': '109989303', 'email': 'Andi@python.com'}
kontak2 = {'nama' : "Ani", 'HP': '933953335', 'email': 'Ani@python.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        # melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")

    elif pilihan == '2':
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor hp kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama':nama, 'HP': HP, 'email': email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")
    elif pilihan == '3':
        # menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus")
    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")