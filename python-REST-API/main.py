
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
#make config
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"
    
#initialize database
# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

resource_fields = {
    'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
    #decorator to return serialized object
    @marshal_with(resource_fields)
    def get(self, video_id):
        #when you query db, gives you instance of class as a result
        result = VideoModel.query.get(id=video_id)
        return result
    
    #arg parsers on how to create new vid
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        #created vid status code
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_not_exist(video_id)
        del videos[video_id]
        return '', 204
        
    def post(self):
        return {"data": 'posted!'}
    
    

# pass params in url
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)