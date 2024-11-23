import qrcode

data=input("enter the data you want to encode: ")
dest= input(
    "Enter the full path destination of where you want your qrcode to be saved: "
)
qr_name = input ('enter the name to save the image: ')
dest = dest.replace("\\", "/")
dest = dest + '/' + qr_name + ".png"
img = qrcode.make(data)
# img=qrcode.make(fit=True)
# img = qrcode.make_image(fill_color="blue", back_color="yellow")
img.save(dest)
print("Success! you can check the folder for the QR code")


