import androidhelper
ans = input("Capture image or not? (y/n)")
if(ans=='y'):
   droid = androidhelper.Android()
   droid.cameraInteractiveCapturePicture('/sdcard/vikas.jpg')
elif(ans=='n'):
   print("Image not taken")
else:
   print("Invalid Symbol")
