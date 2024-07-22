import psycopg2
from flask import Flask
import datetime
from flask import request
import hashlib

conn = psycopg2.connect("")
print('Connected')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS hwids(hwid VARCHAR(255), untill TIMESTAMP WITH TIME ZONE)')
conn.commit()
print('Created table(if not exists) and commited')





app = Flask(__name__)

@app.route('/')
def index():
    return {'code': 403, 'message': 'Forbidden'}

@app.route('/checker', methods=['GET'])
def validation():
    hwid = request.args.get('hwid')
    if not hwid and not isinstance(hwid, str):
        return {'code': 400, 'message': 'Invalid Body'}
    
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
    if not hwid:
        return {'code': 400, 'message': 'Invalid Body'}
    cur = conn.cursor()
    cur.execute('SELECT * FROM hwids WHERE hwid = %s AND untill > %s', (hwid, datetime.datetime.utcnow()))
    vals = cur.fetchone()
    if not vals:
        cur.execute('DELETE FROM hwids WHERE hwid = %s', (hwid,))
        conn.commit()
        cur.close()
        return {'code': 404, 'message': 'Not found'}
    cur.close()
    return genuser

@app.route('/create_hwid', methods=['POST'])
def create():
    json = request.json
    if not isinstance(json, dict):
        return {'code': 400, 'message': 'Invalid Body'}
    if json.get('secure') != 'REPL_SECRET':
        return {'code': 403, 'message': 'Forbidden'}
    
    hwid = json.get('hwid')
    try:
        untill = datetime.datetime.fromisoformat(json.get('untill'))
    except:
        return {'code': 400, 'message': 'Invalid Body'}
    
    cur = conn.cursor()
    cur.execute('INSERT INTO hwids VALUES (%s, %s)', (hwid, untill))
    cur.close()
    conn.commit()
    return {'code': 204}
    

app.run(debug=True)
conn.close()