from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['mydb']
unicorn_collect = db['unicorns']
rides = db['rides']

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/unicorns', methods=['POST'])
def register():
   data = request.get_json()
   name = data.get("name")
   fur = data.get("fur")
   hornLength = data.get("hornLength")
   isBaby = data.get("isBaby")
   owner = data.get("owner")
   unicorn = {
      "name": name,
      "fur": fur,
      "hornLength": hornLength,
      "isBaby": isBaby,
      "owner": owner
   }
   unicorn_collect.insert_one(unicorn)
   return jsonify({"message": "Successful registration"})

@app.route('/unicorns', methods=['GET'])
def unicorns():
   all_unicorn = list(unicorn_collect.find(projection={"_id": False}))
   return jsonify({"unicorns": all_unicorn})

@app.route('/ride', methods=['POST'])
def ride():
   data = request.get_json()
   user = data.get("user")
   unicorn = data.get("unicorn")
   duration = data.get("duration")
   one_ride = {
      "user": user,
      "unicorn": unicorn,
      "duration": duration
   }
   rides.insert_one(one_ride)
   return jsonify({"message": "Registered ride"})

@app.route('/longest_rider/<unicorn_id>', methods=['GET'])
def longest_rider(unicorn_id):
   uni_id_riders = list(rides.find({"unicorn": unicorn_id}).sort("duration", -1))
   if len(uni_id_riders) == 0:
      return "No riders for this unicorn_id", 400
   return jsonify({"user": uni_id_riders[0]["user"]})

if __name__ == '__main__':
   app.run(debug=True)
