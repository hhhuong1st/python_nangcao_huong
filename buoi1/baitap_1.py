with open("btn_2cd.txt","w", encoding="utf-8") as f:
   f.write("Thân em vừa trắng lại vừa tròn \n Bảy nổi ba chìm với nước non")

with open("btn_2cc.txt","w", encoding="utf-8") as f:
   f.write("Rắn nát mặc dầu tay kẻ nặn \n Mà em vẫn giữ tấm lòng son")
 
with open("btn1.txt","a", encoding="utf-8") as f, \
    open("btn_2cd.txt","r", encoding="utf-8") as f1, \
    open("btn_2cc.txt","r", encoding="utf-8") as f2 :
    f.write("Bánh trôi nước")
    f.write("\n")
    f.write(f1.read())
    f.write(f2.read())  
    f.write("\n")
    f.write("Hương")