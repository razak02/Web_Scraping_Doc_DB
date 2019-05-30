from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import MissionToMars_a

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mission_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    Mars_data = mongo.db.Mars_data.find_one()
    return render_template("index.html", Mars_data = Mars_data)


# # @app.route("jsonified")
#     def jsonified)():
#         return jsonify(hello_dict)
# if trouble with 'dict' . route typically returns string only

# collect the data as a list of dictionaries ?


@app.route("/scrape")
def scraper():
   # Mars_data = mongo.db.Mars_data
   #define the name for Mongo Db
    
    Mars_data_mongo = mongo.db.Mars_data 
    Mars_data = MissionToMars_a.scrape()
    Mars_data_mongo.update({}, Mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
