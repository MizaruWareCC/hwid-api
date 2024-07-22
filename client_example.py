import requests
import hashlib

hwid = '1234'

'''
!WARING!
This is being used to fight people using https debuggers to create dynamic, hwid-depended response.
If you will use this, please change this method, because people knowing about this repository can use this method for auto-response.
'''

hashes = []
for letter in hwid:
    sha512 = hashlib.sha512(bytes(letter, encoding='utf-8'))
    hashes.append(sha512.hexdigest())

summ = ''
for hash in hashes:
    summ += hash
genuser = hashlib.sha512(bytes(summ, encoding='utf-8')).hexdigest()


resp = requests.get('http://127.0.0.1:5000/checker', params={'hwid': hwid})

resp = resp.content.decode()

if resp == genuser:
    # If hwid is correct
    print('Correct hwid!11!1!!')
else:
    print('Womp womp')
    print(resp)