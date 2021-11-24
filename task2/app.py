from flask import Flask, jsonify, request
from task1.connect import get_parts

app = Flask(__name__)


@app.route('/')
def get_user():
    try:
        organisation_id = request.args.get('organisation_id')
        if organisation_id:
            row = get_parts(organisation_id)
            resp = jsonify({'dep_people': row})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify('User "organisation_id" not found in query string')
            resp.status_code = 500
            return resp
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run()