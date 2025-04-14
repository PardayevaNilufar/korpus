with open('kitob.txt','r',encoding='utf-8') as f:
    matn=f.read()
    kichik=matn.lower()
royxat=kichik.split()
royxat_matn=matn.split()
print(royxat)


bitta=set(kichik)
print(bitta)
print(len(bitta))


# stop_sozlar=['va','uchun','lekin','ammo','biroq','yo']



# for x in royxat:
#     if x not in stop_sozlar:
#         print(x)

# with open('stop_sozlar','a',encoding='utf-8') as f:
#     f.write(' '.join(royxat_matn))



# stop_sozlar=['va','uchun','lekin','ammo','biroq','yo']
# stop_sozlarsiz_matn=[]



# for x in royxat:
#     if x not in stop_sozlar:
#         stop_sozlarsiz_matn.append(x)

# with open('stop_sozlarsiz_matn','a',encoding='utf-8') as f:
#     f.write(' '.join(stop_sozlarsiz_matn))
