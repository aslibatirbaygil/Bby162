Toplamsaniye= input("saniye girin:")
print ("yıl:",int(int(Toplamsaniye)/31104400))
k= int(Toplamsaniye)%31104400
print ("ay:",int(int(k)/2592000))
l = int(k)%2592000
print ("gün:",int(int(l)/86400))
m = int(l)%86400
print ("saat:",int(int(m)/3600))
n = int(m)%3600
print ("dakika:",int(int(n)/60))
o = int(n)%60
print ("saniye:",o)