import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge


class ImgProcOpencvRos(Node):

    def __init__(self):
        super().__init__('imgproc_opencv_ros')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            qos_profile_sensor_data
        )
        self.publisher = self.create_publisher(Image, 'image_gray', 10)
        self.br = CvBridge()
        self.i = 0  # インスタンス変数として初期化

    def image_callback(self, data):
        source = self.br.imgmsg_to_cv2(data, 'bgr8')
        gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)  # 修正
        _, result = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        result_msg = self.br.cv2_to_imgmsg(result, 'passthrough')
        self.publisher.publish(result_msg)
        self.get_logger().info(f'Publishing image {self.i}')
        self.i += 1  # インクリメント

def main():
    rclpy.init()
    node = ImgProcOpencvRos()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()