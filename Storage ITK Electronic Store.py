print(".::Storage ITK Electronic Store::.")
print("Selamat datang di Gate ITK Electronic Store")
batas = 3
Yansen = "505000" #Ketua Kelompok
Raka = "030999" #Anggota Kelompok
Lutfia = "061000"   #Anggota Kelompok
Dhea = "000000" #Anggota Kelompok
Arjunita ="120600"  #Anggota Kelompok
while(batas>0):
    pin = input("Masukan Password:")
    if(pin==Yansen or Raka or Lutfia or Dhea or Arjunita):
        print("Selamat Datang !!!")
        print("Silahkan pilih:")
        batas = 0
        print("1.Lihat Code")
        print("2.Menarik Barang")
        Coek= input("Silahkan pilih:")
        if(Coek=="1"):
            print(".::Selamat Datang di List Code ITK Electronic::.")
            print("A.Processor")
            print("B.PC Component")
            Code=input("Masukan Code yang di inginkan:")
            Batas=1000
            while(Batas>0):
                if(Code=="A" and "processor" and "Processor"):
                    print("Intel")
                    print("AMD")
                    Merek=input("Pilih jenis Processor:")
                    if(Merek=="Intel"):
                        print("Intelcore I3 Generasi K8 =I3K8")
                        print("Intelcore I5 Generasi K8 =I5K8")
                        print("Intelcore I7 Generasi K8 =I7K8")
                        print("Intelcore I5 Generasi F9 =I5F9")
                        print("Intelcore I7 Generasi F9 =I7F9")
                        print("Intelcore I9 Generasi X9 =I9X9")
                    elif(Merek=="AMD"):
                        print("AMD Ryzen 3= AMDR3")
                        print("AMD Ryzen 5= AMDR5")
                        print("AMD Ryzen 7= AMDR7")
                    else:
                        print("Barang tidak diketahui")
                        print("Akun Automatis telah Logout")
                        break

                elif(Code=="B" and "PC Component"):
                    print("RAM 2GB = RAM2")
                    print("RAM 4GB = RAM4")
                    print("RAM 8GB = RAM8")
                    break
                else:
                    print("Barang tidak diketahui")
                    print("Akun Telah Logout Secara Automatis!!!")
                    break
            else:
                print ("Akun Secara Automatis telah Log Out")
                break;
        elif(Coek=="2"):
            #Intel
            I3K8 = ["Intelcore I3 Generasi 8350K","Rp2.750.000","Rp2.950.000",21]
            I5K8 = ["Intelcore I5 Generasi 8600K","RP3.925.000","Rp4.125.000",17]
            I7K8 = ["Intelcore I7 Generasi 8700K","Rp6.000.000","Rp6.200.000",10]
            I5F9 = ["Intelcore I5 Generasi 9400F","Rp2.240.000","Rp2.640.000",19]
            I7F9 = ["Intelcore I7 Generasi 9900F","Rp6.000.000","Rp6.400.000",12]
            I9X9 = ["Intelcore I9 Generasi 9900X","Rp15.825.000","Rp16.825.000",5]
            #AMD
            AMDR3 = ["AMD Ryzen 3","Rp1.300.000","Rp1.500.000",18]
            AMDR5 = ["AMD Ryzen 5","Rp2.300.000","Rp2.600.000",15]
            AMDR7 = ["AMD Ryzen 7","Rp4.500.000","Rp4.800.000",10]
            #RAM
            RAM2 = ["RAM 2 GB DDR4","Rp150.000","Rp250.000",30]
            RAM4 = ["RAM 4 GB DDR4","Rp250.000","Rp350.000",16]
            RAM8 = ["RAM 8 GB DDR4","Rp500.000","Rp700.000",12]
            Batas = 101010101010
            while (Batas>0):
                Product = input("Masukan barang yang ingin di tarik:")
                if(Product=="I3K8"):
                    X = I3K8
                elif(Product=="I5K8"):
                    X = I5K8
                elif(Product=="I7K8"):
                    X = I7K8
                elif(Product=="I5F9"):
                    X = I5F9
                elif(Product=="I7F9"):
                    X = I7F9
                elif(Product=="I9X9"):
                    X = I9X9
                elif(Product=="RAM2"):
                    X = RAM2
                elif(Product=="RAM4"):
                    X = RAM4
                elif(Product=="RAM8"):
                    X = RAM8
                print("Info Produk : ",X[0])
                print("Harga Beli : ",X[1])
                print("Harga Jual : ",X[2])
                print("Jumlah Barang : ",X[3])
                Yolo = str(input("Tarik Barang? (ya/tidak) : "))
                if Yolo == 'ya' :
                    Next = int(input("Berapa yang ingin ditarik?: "))
                    X[3]-= Next
                    print("Total Barang : ",X[3])
                    print("Terima Kasih!!")
                else:
                    print("Terima Kasih!!")
        else:
            print("Akun Telah Logout Secara Automatis!!!")
    else:
        batas-=1
        if(batas==0):
            print("\033[3l Akun ini Telah di Blokir")
        else:
            print("\033[31m Pin Anda Salah, Mohon Ulangi")
