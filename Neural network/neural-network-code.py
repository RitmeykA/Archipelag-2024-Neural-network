from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

source = 'C:\IMAGES_pomellaz'

results = model.predict(source, conf=0.9)

lalal = 0

f = open('coordinates.txt', 'r')
image = []
image2 = []
x = []
y = []
z = []
o = []


for line in f:
    columns = line.split()
    image.append(columns[0])
    x.append(columns[1])
    y.append(columns[2])
    z.append(columns[3]) 


for i, result in enumerate(results):
    o.append(i+1)
    if len(result.boxes) > 0:
        annotated_image = result.plot()
        cv2.imwrite(f'detected_image_{i}.jpg', annotated_image)
        if (f'image_{i}.jpg'):
            lalal += 1
            image2.append(f'image_{i+1}.jpg')

for k in range (len(image)):
    for j in range (len(image)):
        if image[k] == image2[1]:
            print()
       