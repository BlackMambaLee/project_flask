import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.linux_module.linux_controls import *
from modules.db_module.postgresql import *

app = Flask(__name__)

CORS(app, methods=["GET", "POST", "PUT", "OPTIONS"])

psql = Postgresql()

@app.route('/')
def hello_world():
    return 'hello Flask'

@app.route('/memo', methods=['POST'])
def postMemo():
    data = request.get_json()
    args = (data.get('title'), data.get('content'))
    result = psql.executeInsert('INSERT INTO public.memos (title, content) VALUES (%s, %s) RETURNING id', args)
    return str(result)

@app.route('/memo', methods=['PUT'])
def putMemo():
    data = request.get_json()
    args = (data.get('title'), data.get('content'), data.get('id'))
    result = psql.executeInsert('UPDATE public.memos SET title=%s, content = %s WHERE id = %s', args)
    return str(result)

@app.route('/memo', methods=['GET'])
def getMemo():
    URI = request.args.get('id')

    # URI가 None 또는 빈 문자열인 경우 에러 처리
    if URI is None or URI == '':
        return "Invalid URI", 400
    return jsonify(psql.executeSelect(f'select id, title, content from public.memos where 1=1 and id = {URI}'))
    
@app.route('/memo/all', methods=['GET'])
def getMemoAll():
    return psql.executeSelect('select * from public.memos')


@app.route('/api/v1/<URI>', methods=['POST'])
def api_v1(URI):
    if URI == 'menuList':
        return psql.executeSelect('select * from public.navigate')
    elif URI == 'main':
        return jsonify({'message':'hello world'})
    else:
        return jsonify({'message':'none'})

@app.route('/hostname')
def return_call():
    # data = {'hostname' : 'str(linux_controls.hostname_call())'}
    data = {'hostname' : str(hostname_call())}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')
    # app.run(debug=True, host='127.0.0.1')