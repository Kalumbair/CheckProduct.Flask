from flask import Flask, url_for, request, jsonify, render_template
app = Flask(__name__)

product = []; 

@app.route('/',methods=["GET"])
def hello_world():
    return render_template("index.HTML")

@app.route('/list', methods=['GET'])
def get_product():
    return jsonify(product)

@app.route('/list', methods=['DELETE'])
def delete_product():
    obj = request.get_json()
    i = 0
    while i < len(product):
        if str(product[i]['id']) == obj['id']:
            break
        i+=1
    if i<len(product):
        del product[i]
        return '', 200
    else:
        return '', 400
        
@app.route('/list', methods=['PUT'])
def add_product():
    obj = request.get_json()
    if 'name' in obj and 'kol' in obj and 'count' in obj and int(obj['kol']) and int(obj['count']):
        id=0 if len(product)==0 else product[len(product)-1]['id']+1
        product.append({"id": id,"name": obj['name'],"kol": obj['kol'], "count": obj['count']})
        return '{"id":'+str(id)+'}',200
    return '', 400

@app.route('/list', methods=['POST'])
def edit_product():
    obj = request.get_json()
    if 'id' in obj and 'name' in obj and 'kol' in obj and 'count' in obj and int(obj['kol']) and int(obj['count']):
        i = 0
        while i < len(product):
            if product[i]['id'] == int(obj['id']):
                break
            i+=1

        if i < len(product):
            product[i]['name'] = obj['name']
            product[i]['kol'] = obj['kol']
            product[i]['count'] = obj['count']
            return '', 200
        else:
            return '', 400
    
@app.route('/<filename>', methods=['GET'])
def src(filename=None):
    return render_template(filename)