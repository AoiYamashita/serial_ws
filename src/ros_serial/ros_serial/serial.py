import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import serial

rclpy.init()

node = Node("talker")
pub = node.create_publisher(Int8,"talker",10)

writer = serial.Serial("/dev/ttyACM0",9600,timeout=0.1)

n = 0

def cb():
    global n
    msg = Int8()
    msg.data = n
    pub.publish(msg)
    writer.write(str(n).encode())
    node.get_logger().info("send: %d" % n)
    n = 1 - n

node.create_timer(1,cb)
rclpy.spin(node)
