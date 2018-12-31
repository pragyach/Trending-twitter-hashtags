from flask import Flask,jsonify,request
from flask import render_template
import ast
app = Flask(_name_)
labels = []
values =[]
@app.route("/")
def get_chart_page():
	global labels , values
	labels =[]
	values = []
	return render_template('chart.html',values= values , labels = labels)
@app.route('/refreshData')
def refresh_graph_data():
	global labels, values
	print("labels now:" + str(labels))
	print("data now:" + str(values))
	return jsonify(sLabel = labels , sData = values)
@app.route('/updateData' , methods =['POST'])
def update_data():
	