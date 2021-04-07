#pip install boto3
#pip install opencv-python

import cv2
import boto3
#webcam photo click
cap = cv2.VideoCapture(0)
myphoto = "vishal.jpg"
ret , photo = cap.read()
cv2.imwrite( myphoto , photo)
cap.release()

#using aws s3 service using python boto3 library
region = "ap-south-1"
#bucket should be present in aws s3
bucket = "awsaiworkshp"
myphoto = "vishal.jpg"
upimage = "file.jpg"
s3 = boto3.resource('s3')
s3.Bucket(bucket)
s3.Bucket(bucket).upload_file(myphoto , upimage)
rek = boto3.client('rekognition' , region )
response_face = rek.detect_faces(
     Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
          }
      },
    Attributes = ['ALL']
)
import os
if response_face['FaceDetails'][0]['Smile']['Value'] == False:
    os.system("rhythmbox-client --play")
    x = input("Enter p to pause:")
    if ( x == "p"):
      os.system("rhythmbox-client --pause")