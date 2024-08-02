from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#配置数据库信息
# 数据库：数据库引擎：//数据库用户名：密码@数据库地址/数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nealTest:Neal%40123456@47.120.57.142:3306/myData'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)
    task_detail = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.task_name


if __name__ == '__main__':
    with app.app_context():
        # #创建数据表
        # db.create_all()

        # # 实例化类，添加数据存到表中
        # data = User(id=100, username="tester01", email="tester01@163.com")
        # # 把类添加到sqlalchemy中
        # db.session.add(data)
        # # 提交到数据库
        # db.session.commit()

        #查询数据
        result = User.query.filter_by(id=100).first()
        print(result)

    app.run(debug=True)

