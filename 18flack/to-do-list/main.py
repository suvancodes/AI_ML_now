from flask import Flask, jsonify, request

items = [
    {'id': 1, 'name': 'abc', 'description': 'this is the item 1'},
    {'id': 2, 'name': 'XYZ', 'description': 'this is the item 2'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to sample TO DO list'

# GET: Retrieve all items
@app.route('/item', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by id
@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(item)

# POST: Create a new task
@app.route('/item', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_id = items[-1]['id'] + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an item
@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

if __name__ == "__main__":
    app.run(debug=True)
