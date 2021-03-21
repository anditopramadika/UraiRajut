
def urai(kata):
    a = ''
    for i in range(len(kata)):
        for j in range(0,i+1):
            a += kata[j]
    return a

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print('')
print('')

def rajut(kata):
    b = ''
    awal = 2
    tambah = 1
    #Aritmatika = 1,3,6,10,15,21

    while tambah <= len(kata):
        b += kata[tambah-1]
        tambah += awal
        awal += 1
    return b
    
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))