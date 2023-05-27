#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

<<<<<<< HEAD
def capture_image():
    # Initialize the ROS node
    rospy.init_node('image_node', anonymous=True)
=======
<<<<<<< HEAD
def camera_publisher():
    # Inicializar el nodo de ROS
    rospy.init_node('camera_publisher', anonymous=True)
>>>>>>> 617bf7a62f862070743bf502e15df852ab36596c

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

<<<<<<< HEAD

    # Release resources
=======
=======
def capture_image():
    # Inicializar el nodo ROS
    rospy.init_node('webcam_node', anonymous=True)

    # Crear el objeto CvBridge
    bridge = CvBridge()

    # Acceder a la webcam
    cap = cv2.VideoCapture(0)

    # Crear el publicador para el topico de imagenes capturadas
    image_pub = rospy.Publisher('captured_image', Image, queue_size=10)


    rate = rospy.Rate(10)  # Frecuencia de publicacion en Hz

    while not rospy.is_shutdown():
        # Capturar una imagen de la webcam
        ret, frame = cap.read()

        if not ret:
            rospy.logwarn("Error al capturar la imagen desde la camara")
            continue

        # Convertir la imagen de OpenCV a formato de mensaje de ROS
        image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publicar la imagen en el topico
        image_pub.publish(image_msg)


>>>>>>> 62fd95462e0acf9b71ab347d8a3ac46d16070d11
    # Liberar los recursos
>>>>>>> 617bf7a62f862070743bf502e15df852ab36596c
    cap.release()

if __name__ == '__main__':
    try:
<<<<<<< HEAD
        capture_image()
=======
<<<<<<< HEAD
        camera_publisher()
=======
        capture_image()
>>>>>>> 62fd95462e0acf9b71ab347d8a3ac46d16070d11
>>>>>>> 617bf7a62f862070743bf502e15df852ab36596c
    except rospy.ROSInterruptException:
        pass
