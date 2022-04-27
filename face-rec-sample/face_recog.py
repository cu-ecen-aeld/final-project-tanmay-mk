######### source : https://github.com/ageitgey/face_recognition ############################

##########################Importing libraries required for the program #############################
import face_recognition
import cv2
import numpy as np
from PIL import Image
import serial
import os,time

sim800l = serial.Serial('/dev/ttyAMA0', baudrate = 9600,timeout=1)

previous ="Unknown"
count=0

###########################code for face recognition started##############################

#print("[INFO]..........face recognition started") 

#frame = (video_capture, file)
file = 'image.jpg'

# load the picture whose face has to be recognised.
tanmay_image = face_recognition.load_image_file("/home/pi/Desktop/face-rec-sample/photos/tanmay.jpg")
tanmay_face_encoding = face_recognition.face_encodings(tanmay_image)[0]

varun_image = face_recognition.load_image_file("/home/pi/Desktop/face-rec-sample/photos/varun.jpg")
varun_face_encoding = face_recognition.face_encodings(varun_image)[0]

amey_image = face_recognition.load_image_file("/home/pi/Desktop/face-rec-sample/photos/amey.jpg")
amey_face_encoding = face_recognition.face_encodings(amey_image)[0]

# start your webcam
video_capture = cv2.VideoCapture(0)

# Create arrays of known face encodings and their names
known_face_encodings = [
    tanmay_face_encoding,
    varun_face_encoding,
    amey_face_encoding
    ]
known_face_names = [
    "Tanmay Kothale",
    "Varun Mehta",
    "Amey Dashaputre"
    ]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

tanmay_string = 'Tanmay Kothale'
varun_string = 'Varun Mehta'
amey_string = 'Amey Dashaputre'

tanmay_flag = False
amey_flag = False
varun_flag = False


#fps = video_capture.get(cv2.CAP_PROP_FPS)
#print("FPS: {0}".format(fps))
#######################################################################################
################infinite loop to recognise face in the frame of the camera############
while True:
        
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #cv2.resizeWindow('Video', 600,600)

    #Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #cv2.imwrite(file, small_frame)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
                face_names.append(name)
                if not tanmay_flag:
                    if best_match_index == 0:
                        with open('names.txt','a') as f:
                            f.write(name)
                            f.write('\n')
                            f.close()
                        tanmay_flag = True
                if not amey_flag:
                    if best_match_index == 1:
                        with open('names.txt','a') as f:
                            f.write(name)
                            f.write('\n')
                            f.close()
                        amey_flag = True
                if not varun_flag:
                    if best_match_index == 2:
                        with open('names.txt','a') as f:
                            f.write(name)
                            f.write('\n')
                            f.close()
                        varun_flag = True
                else:
                    print("Already present!")
                name = ''
                #print(name)   


    process_this_frame = not process_this_frame
    
        # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

            # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        

        # Display the resulting image
    cv2.imshow('Video', frame)
    #cv2.resizeWindow('Video', 600,600)
    
    
        # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
      
video_capture.release()
cv2.destroyAllWindows()

