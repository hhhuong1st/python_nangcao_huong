import os
import shutil
duongdan = "Img.Anh.jpg"
if os.exists(duongdan):
    "Img", "Anh.jpg" = os.path.split(duongdan)
    "Anh", ".jpg" = os.path.splitext("Anh.jpg")
    filemoi = "Anh" + "_1" + ".jpg"
    duongdanmoi = os.path
