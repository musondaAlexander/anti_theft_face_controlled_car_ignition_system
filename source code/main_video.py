import cv2
from simple_facerec import SimpleFacerec
import serial
import time

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

# Setting serial port to COM4 at bard rate of 9600
arduinoPort = serial.Serial('COM11', 9600)

# print  A VALUE IF THE FACE IS DETECTED


def send_data(name):

    if (name == "Unknown"):
        data = "accessDenied"+'\r'
        arduinoPort.write(data.encode())
        print("Access Denied")

        # These are the ID other than your face.
    else:
        data = "accessGranted"+'\r'
        arduinoPort.write(data.encode())
        print("Access Granted")


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # print  A VALUE IF THE FACE IS DETECTED
        send_data(name)
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
