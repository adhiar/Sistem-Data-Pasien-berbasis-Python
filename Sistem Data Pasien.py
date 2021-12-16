import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
def menu_utama():
    print('==================================================================================')
    judul=('Data Pasien Puskesmas Sukamaju')
    judul2=('Menu Utama')
    tengah=judul.center(75)
    tengah2=judul2.center(75)
    print(tengah)
    print(tengah2)
    print('==================================================================================')
    print("Keterangan: untuk memilih menu silahkan tekan sesuai nomor menu yang diinginkan")
    print("1: Input Data Rawat Inap\n2: Data Rawat Inap\n3: Input Data Pelayanan Setiap Poli\n4: Data Pelayanan Setiap Poli\n0: exit")
    t=int(input('\n\nPilih menu:'))
    if t==1:
        input_rawatmenu()
    elif t==2:
        tampilan_rawatmenu()
    elif t==3:
        input_poli()
    elif t==4:
        menu_poli()
    elif t==0:
        print('terimakasih telah menggunakan program ini')
        quit()
def judul_inputdata(a):
    print('==================================================================================')
    judul=('Input Data Pasien%s'%a)
    judul2=('Puskesmas Sukamaju')
    tengah=judul.center(75)
    tengah2=judul2.center(75)
    print(tengah)
    print(tengah2)
    print('==================================================================================')
def judul_data(a):
    print('=================================================================================================================================================================')
    judul=('Data Pasien %s'%a)
    judul2=('Puskesmas Sukamaju')
    tengah=judul.center(135)
    tengah2=judul2.center(135)
    print(tengah)
    print(tengah2)
    print('=================================================================================================================================================================')
def input_isirawat():
    z=int(input("tahun data diambil: "))
    nama=str(input("masukkan nama pasien:"))
    kecamatan_asal=str(input("masukkan kecamatan asal pasien:"))
    alamat=str(input("masukkan alamat lengakp pasien:"))
    nik=str(input("masukkan NIK pasien: "))
    print("Tanggal lahir:(tanggal bulan tahun)")
    a, b, c = int(input('tanggal:')), int(input('bulan:')), int(input('tahun:'))
    tanggal_lahir=("%d/%d/%d"%(a,b,c))
    umur=z-c
    tanya=str(input('apakah pasian memiliki asuransi kesehatan?[Y/N]:'))
    if tanya=="Y" or tanya=="y":
        NoA=int(input('masukkan No.Asuransi: '))
    else:
        NoA='Tidak ada'
    bulan=int(input("bulan masuk rawat inap (dalam format angka): "))
    tanggal=int(input("tanggal masuk rawat inap(dalam format angka): "))
    isian=[]
    isian.append(nama.upper())
    isian.append(kecamatan_asal.upper())
    isian.append(alamat)
    isian.append(nik)
    isian.append(tanggal_lahir)
    isian.append(umur)
    isian.append(NoA)
    isian.append(bulan)
    with open('data rawat inap.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isian)
def tampilan_rawatmenu():
    dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data rawat inap.csv')
    a="Rawat Inap"
    judul_data(a)
    df=pd.DataFrame(dataset)
    urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
    i=urut_df.to_string(index=False)
    print(i)
    plt.rcParams['figure.figsize']=(12,5)
    plt.subplot(1,2,1)
    sns.countplot(dataset['Bulan Masuk'],palette='pastel')
    plt.title('Pasien Rawat Inap Tahun 2021',fontsize=15)
    plt.xlabel('bulan ke-',fontsize=14)
    plt.ylabel('pasien',fontsize=14)
    plt.subplot(1,2,2)
    sns.countplot(dataset['Kecamatan Asal'],palette='pastel')
    plt.title('Persebaran Pasien\nberdasarkan Wilayah',fontsize=15)
    plt.xlabel('Kecamatan Asal',fontsize=14)
    plt.ylabel('pasien',fontsize=14)
    plt.show()
    tanya=str(input('\n\napakah anda ingin menginput data?[Y/N]:'))
    if tanya=="Y" or tanya=="y":
        input_rawatmenu()
        tanya=str(input('apakah anda ingin input data lain?[Y/N]:'))
    if tanya=="N"or tanya=="n":
        menu_utama()
        tanya=str(input('apakah anda ingin input data lain?[Y/N]:'))
def input_rawatmenu():
    a="Rawat Inap"
    judul_inputdata(a)
    input_isirawat()
    tanya=str(input('apakah anda ingin input data lain?[Y/N]:'))
    while tanya=="Y" or tanya=="y":
        judul_inputdata()
        input_isirawat()
        tanya=str(input('apakah anda ingin input data lain?[Y/N]:'))
    while tanya=="N"or tanya=="n":
        menu_utama()
        tanya=str(input('apakah anda ingin input data lain?[Y/N]:'))
def menu_poli():
    print('==================================================================================')
    judul=('Data Pasien Puskesmas Sukamaju')
    judul2=('Menu Pilihan Poli')
    tengah=judul.center(75)
    tengah2=judul2.center(75)
    print(tengah)
    print(tengah2)
    print('==================================================================================')
    print("Keterangan: untuk memilih menu silahkan tekan sesuai nomor menu yang diinginkan")
    print("1: Data Poli Umum\n2: Data Poli Gigi\n3: Data Poli Anak\n4: Pelayanan Laboratorium\n5: Data  dan grafik seluruh Poli dan grafik\n0: kembali ke menu utama")
    t=int(input('\n\nPilih menu:'))
    if t==1:
        dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data Poli Umum.csv')
        a="Poli Umum"
        judul_data(a)
        df=pd.DataFrame(dataset)
        urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
        dat=urut_df.to_string(index=False)
        print(dat)
    if t==2:
        a="Poli Gigi"
        judul_data(a)
        dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data Poli Gigi.csv')
        df=pd.DataFrame(dataset)
        urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
        dat=urut_df.to_string(index=False)
        print(dat)
    if t==3:
        a="Poli Anak"
        judul_data(a)
        dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data Poli Anak.csv')
        df=pd.DataFrame(dataset)
        urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
        dat=urut_df.to_string(index=False)
        print(dat)
    if t==4:
        a="Laboratorium"
        judul_data(a)
        dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data lab.csv')
        df=pd.DataFrame(dataset)
        urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
        dat=urut_df.to_string(index=False)
        print(dat)
    if t==5:
        a="Seluruh Pelayanan"
        judul_data(a)
        dataset=pd.read_csv( 'c:/Users/ACER/Documents/phyton/data Pelayanan.csv')
        a="di Setiap Pelayanan"
        df=pd.DataFrame(dataset)
        urut_df=df.sort_values(by=['Bulan Masuk'],ascending=True)
        dat=urut_df.to_string(index=False)
        print(dat)
        plt.rcParams['figure.figsize']=(10,5)
        plt.subplot(2,2,1)
        sns.countplot(dataset['Bulan Masuk'],palette='pastel')
        plt.title('Pasien 2021',fontsize=15)
        plt.xlabel('bulan ke-',fontsize=12)
        plt.ylabel('pasien',fontsize=12)
        plt.subplot(2,1,2)
        sns.countplot(dataset['Kecamatan Asal'],palette='pastel')
        plt.title('Persebaran Pasien\nberdasarkan Wilayah',fontsize=15)
        plt.xlabel('Kecamatan Asal',fontsize=8)
        plt.ylabel('pasien',fontsize=8)
        plt.xticks(fontsize=8,rotation=5)
        plt.subplot(2,2,2)
        sns.countplot(dataset['Pelayanan'],palette='pastel')
        plt.title('Jumlah Kedatangan Pasien\nBerdasarkan Tujuan Pelayanan',fontsize=14)
        plt.xlabel('Bentuk Pelayanan',fontsize=8)
        plt.ylabel('pasien',fontsize=10)
        plt.subplots_adjust(wspace=0.8,hspace=0.7)
        plt.xticks(fontsize=8,rotation=8)
        plt.show()
    if t==0:
        menu_utama()
    p=str(input('\n\nApakah anda ingin melihat data lain?[Y/N]: ')).upper()
    if p=="Y":
        menu_poli()
    else:
        menu_utama()
def input_poli():
    a=''
    judul_inputdata(a)
    print("Pilih Pelayanan Input Sesuai Pilihan nomor\nket:\n1: Data Poli Umum\n2: Data Poli Gigi\n3: Data Poli Anak\n4: Pelayanan Laboratorium\n0: Ke menu Utama")
    pilih=int(input("\n\nPilih Menu: "))
    if pilih==1:
        isian_poliumum()
        print("Pengisian data selesai....")
        menu_poli()
    if pilih==2:
        isian_poligigi()
        print("Pengisian data selesai....")
        menu_poli()
    if pilih==3:
        isian_polianak()
        print("Pengisian data selesai....")
        menu_poli()
    if pilih==4:
        isian_polilab()
        print("Pengisian data selesai....")
        menu_poli()
    if pilih==0:
        menu_utama()
def input_isianpoli():
    z=int(input("tahun data diambil: "))
    nama=str(input("masukkan nama pasien:"))
    kecamatan_asal=str(input("masukkan kecamatan asal pasien:"))
    alamat=str(input("masukkan alamat lengakp pasien:"))
    nik=str(input("masukkan NIK pasien: "))
    print("Tanggal lahir:(tanggal bulan tahun)")
    a, b, c = int(input('tanggal:')), int(input('bulan:')), int(input('tahun:'))
    tanggal_lahir=("%d/%d/%d"%(a,b,c))
    umur=z-c
    tanya=str(input('apakah pasian memiliki asuransi kesehatan?[Y/N]:'))
    if tanya=="Y" or tanya=="y":
        NoA=int(input('masukkan No.Asuransi: '))
    else:
        NoA='Tidak ada'
    gejala=str(input('Gejala Penyakit/Check Up:'))
    bulan=int(input("bulan kedatangan (dalam format angka): "))
    tanggal=int(input("tanggal kedatangan (dalam format angka): "))
    isian=[]
    isian.append(nama.upper())
    isian.append(kecamatan_asal.upper())
    isian.append(alamat)
    isian.append(nik)
    isian.append(tanggal_lahir)
    isian.append(umur)
    isian.append(NoA)
    isian.append(bulan)
    isian.append(gejala)
    return isian
def isian_poliumum():
    a='Poli Umum'
    judul_inputdata(a)
    isianpoli=input_isianpoli()
    isian=isianpoli+["Poli Umum"]
    with open('data Poli Umum.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isianpoli)
    with open('data Pelayanan.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isian)
def isian_poligigi():
    a='Poli Gigi'
    judul_inputdata(a)
    isianpoli=input_isianpoli()
    isian=isianpoli+["Poli Gigi"]
    with open('data Poli Gigi.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isianpoli)
    with open('data Pelayanan.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isian)
def isian_polianak():
    a='Poli Anak'
    judul_inputdata(a)
    isianpoli=input_isianpoli()
    isian=isianpoli+["Poli Anak"]
    with open('data Poli Anak.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isianpoli)
    with open('data Pelayanan.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isian)
def isian_polilab():
    a='Laboratorium'
    judul_inputdata(a)
    isianpoli=input_isianpoli()
    isian=isianpoli+["Laboratorium"]
    with open('data lab.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isianpoli)
    with open('data Pelayanan.csv', 'a',newline='') as x:
        data = csv.writer(x) 
        data.writerow(isian)
menu_utama()