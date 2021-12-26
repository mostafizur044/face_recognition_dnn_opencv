import os
import cv2
#File Paths

filedir = os.path.dirname(os.path.realpath(__file__))

#Get User Name
name = input("Enter Name: ")

#Create directory
directory = os.path.join(filedir, "dataset", name)

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory _images\{} Successfully Created".format(name))
else:
    print("Directory Already Exists. Continuing With Capture")


#Capture Images
print("Starting Webcam...")
capture = cv2.VideoCapture(0)

image_counter =  1

while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagasde', frame)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        # ESC pressed
        print("Escape hit. Closing Webcam...")
        break
    elif k == 32:
        # SPACE pressed
        print("writing file")
        image_name = "opencv_frame_{}.png".format(image_counter)
        cv2.imwrite(os.path.join(directory, image_name), frame)
        print("{} written!".format(image_name))
        image_counter += 1

capture.release()

cv2.destroyAllWindows()

os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --label output/label.pickle')