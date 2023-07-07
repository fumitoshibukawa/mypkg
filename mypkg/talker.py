#ros2でpythonでノードを書く時のライブラリ(モジュール）
import rclpy
#ノードを作るためのパッケージからNodeというクラスをインポート
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "渋川史人":
        response.age = 21
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

