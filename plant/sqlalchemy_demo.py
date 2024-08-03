from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#配置数据库信息
# 数据库：数据库引擎：//数据库用户名：密码@数据库地址/数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nealTest:Neal%40123456@47.120.57.142:3306/myData'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # def __repr__(self):
    #     return f'<User {self.username} {self.email}>'
    def transformer(self):
        return {
            'id':self.id,
            'username':self.username,
            'email':self.email
        }

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)
    task_detail = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.task_name


class UserServer(Resource):

    def get(self):
        """
        通过接口获取用户信息
        :return: 所有用户信息
        """
        result = User.query.all()
        result = [user.transformer() for user in result]
        return result

    def post(self):
        """
        添加用户
        :return:
        """
        data = User(**request.json)
        db.session.add(data)
        db.session.commit()
        return {'message': 'User added successfully!'}

api.add_resource(UserServer, '/user')


if __name__ == '__main__':
    # with app.app_context():
        # #创建数据表
        # db.create_all()

        # # 实例化类，添加数据存到表中
        # data = User(id=100, username="tester01", email="tester01@163.com")
        # # 把类添加到sqlalchemy中
        # db.session.add(data)
        # # 提交到数据库
        # db.session.commit()

        #查询数据
        # result = User.query.filter_by(id=100).first()
        # print(result)

    app.run(debug=True)

