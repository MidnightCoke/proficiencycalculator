import time
#sinav sonuclari pt1 %10 mte %20 pt2 %15 ete %25
#speaking portfolio %10 writing %15 te %5
pt1 = int(input("Progress 1 testinin sonucunu giriniz. "))

mte = int(input("MTE Vize sinav sonucunu giriniz. "))

pt2 = int(input("Progress 2 testinin sonucunu giriniz. "))

ete = int(input("ETE Final sinav sonucunu giriniz. "))

sp = int(input("Speaking Portfolio notunuzu giriniz. "))

wp = int(input("Writing Portfolio notunuzu giriniz. "))

te = int(input("Teacher Evaluation notunuzu giriniz. "))

exam = float(pt1*0.10) + float(mte*0.20) + float(pt2*0.15) + float(ete*0.25)

teacher = float(sp*0.10) + float(wp*0.15) + float(te*0.05)

fpass = float(exam + teacher)

if fpass >= 65.0 :
        print("Hazirligi gecebilirsiniz " + "Notunuz: " + str(fpass))
        time.sleep(5)

elif fpass < 65.0 :
        print ("Notunuz hazirligi gecmek icin yeterli degil " + str(fpass))
        time.sleep(5) 


