import os
import cv2

imgs = './Images/'; images = []



for img in os.listdir(imgs):
  file_name,ext = os.path.splitext(img)

  if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    fileName = imgs+'/'+img
    images.append(fileName)
    count = len(images)
    print(images)

  frame = cv2.imread(images[0])
  height, width, layer = frame.shape
  size = (width, height)
  
  out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

  for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print('Done')
    


  