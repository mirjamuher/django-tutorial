import os
import qrcode

DIR = os.path.dirname(__file__)
os.chdir(DIR)

# http://eventmanager.mirjamuher.com/checkin/eventid/userid/

for i in range(1, 100):
    event_no = 1
    participant_code = i
    url = f'https://eventmanager.mirjamuher.com/checkin/{event_no}/{participant_code}/'
    img = qrcode.make(url)
    img_name = f'QR_codes/qr_code_{i}.png'
    img.save(img_name)
