import cv2 as cv
import numpy as np
import face_recognition

imgved = face_recognition.load_image_file('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images/vedant_1.jpg')
imgved = cv.cvtColor(imgved, cv.COLOR_BGR2RGB)

imgtest = face_recognition.load_image_file('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images/ronaldo_1.jpg')
imgtest = cv.cvtColor(imgtest, cv.COLOR_BGR2RGB)

#1st Image
faceLoc = face_recognition.face_locations(imgved)[0]
encode_ved = face_recognition.face_encodings(imgved)[0]
cv.rectangle(imgved, (faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,0,255),2)

#2nd Image
faceLoc2 = face_recognition.face_locations(imgtest)[0]
encode_2 = face_recognition.face_encodings(imgtest)[0]
cv.rectangle(imgtest, (faceLoc2[3],faceLoc2[0]),(faceLoc2[1],faceLoc2[2]),(0,0,255),2)

result = face_recognition.compare_faces([encode_ved],encode_2)
facedis = face_recognition.face_distance([encode_ved],encode_2)
cv.putText(imgtest,f'{result} {round(facedis[0],2)}',(50,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

print(result)
print(facedis)

cv.imshow('Vedant',imgved) 
cv.imshow('Veda1nt',imgtest) 
cv.waitKey(0)