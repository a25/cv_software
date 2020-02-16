import cv2
import pytesseract
import numpy as np
import csv
import sys
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imageName='assets\\che.jpeg'
img=cv2.imread(imageName)
if(img is not None):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,100,apertureSize = 5)
    cv2.imshow("imgage1",edges)
    lines = cv2.HoughLines(edges,1,np.pi/180, 300)#400
    if lines is not None:
        for el in lines:
            for r,theta in el: 
                
                # Stores the value of cos(theta) in a 
                a = np.cos(theta) 
            
                # Stores the value of sin(theta) in b 
                b = np.sin(theta) 
                
                # x0 stores the value rcos(theta) 
                x0 = a*r 
                
                # y0 stores the value rsin(theta) 
                y0 = b*r 
                
                # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
                x1 = int(x0 + 1000*(-b)) 
                
                # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
                y1 = int(y0 + 1000*(a)) 
            
                # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
                x2 = int(x0 - 1000*(-b)) 
                
                # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
                y2 = int(y0 - 1000*(a)) 
                
                # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
                # (0,0,255) denotes the colour of the line to be  
                #drawn. In this case, it is red.  
                cv2.line(img,(x1,y1), (x2,y2), (255,255,255),2)
    cv2.imshow("imgage",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    text=pytesseract.image_to_string(img)
    print(text)
    x=text.strip().split('\n')
    with open('protagonist.csv', 'w') as file:
        writer = csv.writer(file)
        for el in (x):
            reload(sys)
            sys.setdefaultencoding( "latin-1" )
            j=[str(val) for val in el.split(' ') if val!='|']
            writer.writerow(j)
            #for el1 in j:
            #    print(el1.encode("utf-8"))
else:
    print('Image is Invalid')



