import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

Priyanshu_image = face_recognition.load_image_file("Priyanshu.jpg")
Priyanshu_encoding = face_recognition. face_encoding(Priyanshu_image)[0]

Abhiman_image = face_recognition.load_image_file("Abhiman.jpg")
Abhiman_encoding = face_recognition. face_encoding(Abhiman_image)[0]

Praveen_image = face_recognition.load_image_file("Praveen.jpg")
Praveen_encoding = face_recognition. face_encoding(Praveen_image)[0]

Rohit_image = face_recognition.load_image_file("Rohit.jpg")
Rohit_encoding = face_recognition. face_encoding(Rohit_image)[0]

Saurav_image = face_recognition.load_image_file("Saurav.jpg")
Saurav_encoding = face_recognition. face_encoding(Saurav_image)[0]


known_face_encoding = [
Priyanshu_encoding,
Abhiman_encoding,
Praveen_encoding,
Rohit_encoding,
Saurav_encoding
]


known_faces_names = [
"Priyanshu",
"Abhiman",
"Praveen",
"Rohit"
"Saurav"
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")



f = open(current_date+'.csv','w+',newline = '')
Inwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_loction(rgb_small_frame)
        face_encodings = face_recognition.face_encoding(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_recognition:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ''
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    Inwriter.writerow([name, current_time])

    cv2.imshow('attendence system', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
