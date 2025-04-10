import qrcode

    #  ╔══════════════════════════╗
    #  ║   ✨QR CODE incoder ✨  ║
    #  ╚══════════════════════════╝

Data = "Python Developer | Ilsa Ubaid | GIAIC Q-3"

#for simple QR code

img = qrcode.make(Data)
img.save('C:/Users/A.K Com/OneDrive/Documents/Q3/new/myqrcode.png')

#customized QR code

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)

#will add my data in qrcode by converting it into chunks
qr.add_data(Data)

qr.make(fit = True) #find the best fit for the data to avoid data overflow errors.

#Make an image from the QR Code data.
img = qr.make_image(fill_color = "green", back_color = "yellow")

img.save('C:/Users/A.K Com/OneDrive/Documents/Q3/new/myqrcode1.png')


    #  ╔══════════════════════════╗
    #  ║   ✨QR CODE decoder ✨  ║
    #  ╚══════════════════════════╝

import cv2 #library to decode

#Loads the QR Code Image
img = cv2.imread('C:/Users/A.K Com/OneDrive/Documents/Q3/new/myqrcode1.png')

#Initialize QR Code Detector
detector = cv2.QRCodeDetector()

# Detect and Decode
data, _, _ = detector.detectAndDecode(img)

print("Decoded Data: ",data)