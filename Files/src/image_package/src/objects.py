#!/usr/bin/env python3
import rospy
import ctypes
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from cv_bridge import CvBridge
import cv2

coordLibrary = ctypes.CDLL("/home/meli/Documents/MedioTermino/Files/src/image_package/src/library/lib.so")

class Objects:
    # Subscribe and Publish on Ros topics
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("image_topic", Image, self.objects)
        self.pub_coord = rospy.Publisher("object_topic", PointStamped, queue_size=10)
        self.coord = PointStamped()
        self.coord.header.frame_id = "camera_frame"

    # Proccess image to detect objects
    def objects(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_green = (40, 110, 40)
        upper_green = (80, 255, 200)
        mask = cv2.inRange(hsv_image, lower_green, upper_green)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        coordY = ctypes.c_float(0)
        coordX = ctypes.c_float(0)
        coordZ = ctypes.c_float(0)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                coordY.value = (y + h) / 2
                coordX.value = (x + w) / 2
                coordLibrary.calculateCoords(ctypes.byref(coordX), ctypes.byref(coordY), ctypes.byref(coordZ))

                self.coord.point.x = coordX.value
                self.coord.point.y = coordY.value
                self.coord.point.z = coordZ.value
                self.coord.header.stamp = rospy.Time.now()
                self.pub_coord.publish(self.coord)

        cv2.imshow("Object Camera", cv_image)
        cv2.waitKey(1)

# Initializes the ROS node and starts to detect objects
def main():
    rospy.init_node('object_node')
    detector = Objects()
    rospy.spin()


if __name__ == '__main__':
    main()