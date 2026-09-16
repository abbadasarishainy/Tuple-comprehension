list=[1,2,3,4,5]
dtpl=tuple(i**2 for i in list)
print(dtpl)

lst=[-12,84,11,22,-3,0,-25]
pstv_tpl=tuple(i for i in lst if i>0)
print(pstv_tpl)
