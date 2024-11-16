#make image publisher in ros2 ,python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher=self.create_publisher(Image,'camera/image_raw',10)
        self.timer=self.create_timer(0.5,self.publish_image)
        self.cap=cv2.VideoCapture(0)
        self.i=0
        self.br=CvBridge()

    def publish_image(self):
        ret,img=self.cap.read()
        msg=self.br.cv2_to_imgmsg(img)
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing image{self.i}')
        self.i+=1
    
def main():
    rclpy.init()
    node=ImagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
    cv2.destroyAllWindows()