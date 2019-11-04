modal_awal=100000000
sum=0
y=0
laba = [int(0), int(0), int(modal_awal) * .1, int (modal_awal) * .1, int(modal_awal) * .5, int(modal_awal) * .5, int(modal_awal) * .5, int(modal_awal) * .2]

print("Modal awal seorang pengusaha:", modal_awal)

for i in laba :
    sum = sum+i
    y+=1

    print("Laba / keuntungan bulan ke-",y,"sebesar:", i)

print("Total laba / keuntungan selama 8 bulan sebesar:", sum)
