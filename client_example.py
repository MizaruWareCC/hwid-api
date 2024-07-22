import requests
import hashlib

hwid = '2'

def generate_hash(string):
    hashes = []
    for letter in string:
        sha512 = hashlib.sha512(bytes(letter, encoding='utf-8'))
        hashes.append(sha512.hexdigest())

    summ = ''
    for hash in hashes:
        summ += hash

'''
!WARING!
This is being used to fight people using https debuggers to create dynamic, hwid-depended response.
If you will use this, please change this method, because people knowing about this repository can use this method for auto-response.
'''


genuser = generate_hash(hwid)


resp = requests.get('http://127.0.0.1:5000/checker', params={'hwid': hwid})

resp = resp.content.decode()

if resp == genuser:
    # If hwid is correct
    print('Correct hwid!11!1!!')
else:
    print('Womp womp')
    print(resp)