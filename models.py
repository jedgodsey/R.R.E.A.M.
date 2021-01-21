from app import db, marshmallow

class Post(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    profile_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    def __init__(self, name, profile_name, email):
        self.name = name
        self.profile_name = name
        self.email = email

    @classmethod
    def create_post(cls, name, profile_name, email):
        new_post = Post(name, profile_name, description)
        try:
            db.session.add(new_post)
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception('Session rollback')
        return post_schema.jsonify(new_post)

    @classmethod
    def get_post(cls, postid):
        post = Post.query.get(postid)
        return post_schema.jsonify(post)

class PostSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'profile_name', 'email')

post_schema = PostSchema()
posts_schema = PostSchema(many=True)




if __name__ == 'models':
    db.create_all()
