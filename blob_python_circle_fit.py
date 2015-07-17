#By Sachin Kolachana
import sys
import os
import fnmatch
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import sys
import csv
count=0

path = '/home/tim/CMU/SunTracker/Full_Scan_Data'
numfiles= len(fnmatch.filter(os.listdir(path), 'fileCV*.BMP'))
tData = np.zeros((numfiles,5));
files = []


for name in os.listdir(path):
    file = os.path.join(path, name)
    if os.path.isfile(file):
        files.append(file)

fnum = 2
for filename in files:
    fnum = fnum+1
    filename = "fileCV%d.BMP"%(fnum)
    filename = os.path.join(path, filename)
    print filename
    im = cv2.imread(filename)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    dist=np.zeros((imgray.shape[0],imgray.shape[1]))
    size_grayscale=np.shape(im)
    max_value=max(im.flatten()) #which is 255

    min_value=max_value-5

    ret,thresh = cv2.threshold(imgray,min_value,max_value,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    x = []
    for i in range(len(contours)):
        x.append(cv2.contourArea(contours[i]))
	
    #print max(x)
    MaxIndex= x.index(max(x))
    cnt = contours[0] 
    cv2.drawContours(im,contours,-1,(0,255,0),1)
# for i in range(0,5):
  # Area[i]=cv2.contourArea(contours[i])
    for ind_y in range(240):
     for ind_x in range(320):
      dist[ind_y,ind_x] = cv2.pointPolygonTest(contours[MaxIndex],(ind_y,ind_x),True)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
    cv2.circle(im,(maxLoc[1],maxLoc[0]),int(maxVal),(0, 255, 0),2)
    centroid_x=maxLoc[0]
    centroid_y=maxLoc[1]
    cv2.circle(im,(int(centroid_y),int(centroid_x)),1,(255,0,0),-1)
# print contours[29][0]
#cv2.imshow("Range", mask)
# print mean
    # cv2.imshow("image",im)
    # cv2.waitKey(0)
    H,W= np.shape(imgray)
    X=np.linspace(1, H, 5)
# cv2.waitKey(0)
# [H,W] = size(datagray);
    for k in X:
       lineX = [W/2, W/2]
       lineY = [k ,k]
    # %if plotting
    cv2.circle(im,(int(centroid_x),int(centroid_y)),1,(0,0,255),-1)
        
    # cv2.imshow("image",im)
    # cv2.waitKey(0)
        # %end
    # end
    halfangle=45
    
   
    v=[(centroid_x),(centroid_y)]
    t = np.linspace(0,W,5)
    elDist = np.linalg.norm(v)
    elevation = elDist/(W/2)*halfangle
    angle=math.atan2((centroid_y-H/2),(centroid_x-W/2))-math.pi/2
   
    
    
    cv2.imshow("image",im)
    cv2.waitKey(0)
  
    tData[count,0]=count
    
    tData[count,1] = angle*180/(math.pi)
    
    tData[count,2] = elevation
    tData[count,3]=centroid_x
    tData[count,4]=centroid_y
    
    count=count+1

# np.savetxt('imageDatafrcrobot2015june26.csv', tData, delimiter = ",")
       



# print tData

# data = [np. tData[:,0], np.tData[:,1],  tData[:,2]]
       
# a.writecolumns(data)
# b.close()

    
    #csvwrite('AngleData.csv',tData);
	 #plot(t,slope*t+(H/2-slope*W/2),'Color','w');
    # %if plotting
	 # plot(t,slope*t+(H/2-slope*W/2),'Color','w');
 #cv2.circle(im,t,slope*t+(H/2-slope*W/2), 1, (0,0,255), 1)
    # %end
    # %angle due north with respect to image
# angle=math.tan(slope)-3.14/2
    # %fprintf('Azimuth Angle of %d:\n',numfiles);
# %     fprintf('Azimuth:   %.2f degrees\n',angle*180/pi);
# %     fprintf('Elevation: %.2f degrees\n',elevation);
    # %fprintf('\t%d radians\n',angle);












