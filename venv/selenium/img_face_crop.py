# 파일 설명

import os
import glob

selected_path = "C:/Users/dlxog/Desktop/포켓몬_얼굴인식_닮은꼴_프로젝트/연예인 사진 모음/원본/30. 피카츄/아이유"


# 01. 이미지 파일명 변경하기(출처 : https://hogni.tistory.com/35)
img_name_change_file_path = selected_path
img_name_change_file_name = os.listdir(img_name_change_file_path)
img_name_change_i = 1

for name in img_name_change_file_name :
    src = os.path.join(img_name_change_file_path, name)
    dst = str(img_name_change_i) + ".jpg"
    dst = os.path.join(img_name_change_file_path, dst)
    try:
        os.rename(src,dst)
    except:
        pass

    img_name_change_i += 1


# 03. 폴더 생성 (crop 한 이미지 저장용도)
cropped_folder = "cropped_" + os.path.basename(selected_path)
if not os.path.isdir(cropped_folder) :
    os.mkdir(cropped_folder)

# 02. 얼굴 인식 + Crop (출처 : https://sulastri.tistory.com/1 외 구글링)
import cv2
import numpy as np # cv에서 경로를 한글을 인식 못함, 그래서 사용

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 이미지 불러오기 
imgnum = 1
path = selected_path
max_imgnum = os.listdir(path) # 경로 안에 파일을 리스트 형태로 보여줌 / len 써서 숫자화

while imgnum <= len(max_imgnum) :
    img_name = str(imgnum) + ".jpg"
    full_path = path + "/" + img_name
    img_array = np.fromfile(full_path, np.uint8)

    img = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:

      # 얼굴 사각형 표시 - 주석처리
      cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

      # 얼굴 crop 부분 
      cropped = img[y - int(h/8):y + h + int(h/8), x - int(w/8):x + w + int(w/8)]
      
      # crop 한 사진 저장
      new_img_name = cropped_folder + "/" + "cropped_"+str(imgnum)+".png"
      extension = os.path.splitext(new_img_name)[1] # 이미지 확장자\
      try :
          result, encoded_img = cv2.imencode(extension, cropped)
      except:
          pass
 
      if result:
         with open(new_img_name, mode='w+b') as f:
           encoded_img.tofile(f)


    imgnum = imgnum + 1 
