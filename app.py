from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from db_models.workout import connect_db, Workout, db

app = Flask(__name__)
connect_db(app)
CORS(app)
api = Api(app)


class Workout_api(Resource):
    def get(self, workout_id=None):
        # Workout.query.all()
        result_dict = [u.to_json() for u in Workout.query.all()]
        print(result_dict)
        return result_dict, 200

    def post(self, workout_id=None):
        print(request.json)
        body = request.json
        print(body['dia'])
        newWorkout = Workout()
        newWorkout.dia = body['dia']
        newWorkout.treino = body['treino']
        newWorkout.duracao = body['duracao']

        db.session.add(newWorkout)
        db.session.commit()
        # models.Workout.query().delete()

        print(newWorkout)
        return "Success", 201

    def delete(self, workout_id):
        del_id = Workout.query.filter_by(id=workout_id).first()
        db.session.delete(del_id)
        db.session.commit()
        return "Success", 204


api.add_resource(Workout_api, '/workout','/workout/<workout_id>')


if __name__ == '__main__':
    app.run(debug=True)
