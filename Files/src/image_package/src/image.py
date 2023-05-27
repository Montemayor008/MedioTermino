#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

<<<<<<< HEAD
def camera_publisher():
    # Inicializar el nodo de ROS
    rospy.init_node('camera_publisher', anonymous=True)

    # Crear un objeto CvBridge
    bridge = CvBridge()

    # Crear un objeto VideoCapture para capturar imágenes desde la cámara
    cap = cv2.VideoCapture(0)

    # Crear un objeto ImagePublisher para publicar imágenes en el tópico de ROS
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)

    # Definir la frecuencia de publicación
    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        # Capturar la imagen desde la cámara
        ret, frame = cap.read()

        # Comprobar si la captura de la imagen fue exitosa
        if not ret:
            rospy.logwarn("Error al capturar la imagen desde la cámara")
            continue

        # Convertir la imagen de OpenCV a un mensaje de imagen de ROS
        image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publicar el mensaje de imagen en el tópico de ROS
        image_pub.publish(image_msg)

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
    cap.release()

if __name__ == '__main__':
    try:
<<<<<<< HEAD
        camera_publisher()
=======
        capture_image()
>>>>>>> 62fd95462e0acf9b71ab347d8a3ac46d16070d11
    except rospy.ROSInterruptException:
        pass
