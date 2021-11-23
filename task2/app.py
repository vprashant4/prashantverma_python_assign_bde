from flask import Flask, jsonify, request 
import psycopg2 
import psycopg2.extras
from task1.config import config
 
app = Flask(__name__)
 
conn = None
params = config()     
conn = psycopg2.connect(**params)
 
 
@app.route('/') 
def get_user():
    try:
        organisation_id = request.args.get('organisation_id')
        if organisation_id:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            #cur.callproc('test_sch.prashantverma_return_dep_people', (organisation_id,)
            cur.execute("SELECT * FROM test_sch.prashantverma_return_dep_people(%s); ",(organisation_id,))
            row = cur.fetchone()
            resp = jsonify(row)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify('User "organisation_id" not found in query string')
            resp.status_code = 500
            return resp
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        conn.close()


if __name__ == "__main__":
    app.run()

