from flask import Flask, request, jsonify
from conveter import *
from flask_cors import CORS
import markdown


with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = markdown.markdown(readme_file.read())

app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
    return readme


@app.route("/convert", methods=["GET"])
def convert():
    type = request.args.get("type")
    value = float(request.args.get("value"))
    from_unit = request.args.get("from")
    to_unit = request.args.get("to")

    if type == "length":
        result = {
            "converted_value": length_convert(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }
    elif type == "temp":
        result = {
            "converted_value": temp_convert(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }
    elif type == "area":
        result = {
            "converted_value": convert_area(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }
    elif type == "speed":
        result = {
            "converted_value": convert_speed(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }
    elif type == "mass":
        result = {
            "converted_value": convert_mass(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }
    elif type == "data":
        result = {
            "converted_value": convert_data(value, from_unit, to_unit),
            "value": value,
            "from": from_unit,
            "to": to_unit,
        }

    if result is not None:
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid conversion"}), 400


if __name__ == "__main__":
    app.run(debug=True)
