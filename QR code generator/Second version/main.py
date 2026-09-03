import qrcode
import os
image_path = r'C:\Users\Потребител\Desktop\REPO\Personal-projects\QR code generator\Second version'

while True:

    qr_code_type = input('Please enter the URL or PNG to convert QR code: ')

    if qr_code_type.startswith('https://') or qr_code_type.startswith('http://'):
        img = qrcode.make(qr_code_type)
        image_directory = os.listdir(image_path)
        if 'qr.png' in image_directory:
            while True:
                new_name = input('Please enter new name for the png file: ')
                if new_name.endswith('.png'):
                    img.save(new_name)
                    break
                print("enter valid name that ends with '.png'")
            break
        img.save('qr.png')
        break
    elif qr_code_type.endswith('.png'):
        image_to_qr_path = image_path + qr_code_type
        if os.path.exists(image_to_qr_path):
            pass

    print('Please enter valid URL or PNG!')