import qrcode

qr_code_info = input("Please type in what you want your QR code to contain: ")
qr_code_file_name = input("Please type in the file name: ")

qr_code_file = f"{qr_code_file_name}.png"
qr_code_img = qrcode.make(qr_code_info)

qr_code_img.save(qr_code_file)
