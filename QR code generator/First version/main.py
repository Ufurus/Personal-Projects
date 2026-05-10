# simple code to generate PNG of QR code for a link.

import qrcode

img = qrcode.make(input('Please enter URL to make a png for: ')) # takes input in order to convert pasted link to a png.

img.save('qr.png') # this save the png. Since it is not specified, it saves the image where the main file is located.