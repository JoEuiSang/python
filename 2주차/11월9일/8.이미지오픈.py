# rb / wb/ ab / rt / wt
#읽기 / 쓰기/이어쓰기/

img1= open('naeun.jpg','rb')
img2=open('c.jpg','wb')

data = img1.read()
img2.write(data)

img1.close()
img2.close()