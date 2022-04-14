import cv2 as cv2
vid = cv2.VideoCapture("video.mp4")
i = 0

while vid.isOpened():
    ret , frame = vid.read()
    if ret == False:
        break
    cv2.imwrite("/Users/anasarodake/DataSpell/projects/dsProject/bilder/" + str(i) + ".jpg",frame)
    i= i+1

vid.release()
cv2.destroyAllWindows()


#%%

#%%
