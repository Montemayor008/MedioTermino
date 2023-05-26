#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

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


    # Liberar los recursos
    cap.release()

if __name__ == '__main__':
    try:
        capture_image()
    except rospy.ROSInterruptException:
        pass
