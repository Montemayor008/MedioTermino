#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def capture_image():
    # Initialize the ROS node
    rospy.init_node('image_node', anonymous=True)

    # Create CvBridge object
    bridge = CvBridge()

    # Access webcam
    cap = cv2.VideoCapture(0)

    # Publish the image in a topic
    image_pub = rospy.Publisher('image_topic', Image, queue_size=10)

    # Publish Rate
    rate = rospy.Rate(10)  


    while not rospy.is_shutdown():
        # Capture Image
        ret, frame = cap.read()

        #if not ret:
        #    rospy.logwarn("Error al capturar la imagen desde la camara")
        #    continue

        # Convert image to ROS format
        image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publish image on topic
        image_pub.publish(image_msg)


    # Release resources
    cap.release()

if __name__ == '__main__':
    try:
        capture_image()
    except rospy.ROSInterruptException:
        pass
