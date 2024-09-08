import numpy as np
import cv2

config_dict = {
	'1961':{
		'invert': False,
		'blackwhite':False,
		'thicken_font':[False,1,1], # kernel size, number of iterations
		'thin_font':[False,1,1], # kernel size, number of iterations
		'deskew':False,
		'noise_removal':[False,1,3] # kernel size, medianBlur kernel size
	},
	'2004':{
		'invert': False,
		'blackwhite':False,
		'thicken_font':[False,1,1], # kernel size, number of iterations
		'thin_font':[False,1,1], # kernel size, number of iterations
		'deskew':False,
		'noise_removal':[False,1,3] # kernel size, medianBlur kernel size
	}

}

def getSkewAngle(image) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = image.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)
    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)
    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

def rotateImage(image, angle: float):
	# Rotate the image around its center
    newImage = image.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage			

def pre_process(year:str, temp_path:str):
	image = cv2.imread(temp_path)

	config = config_dict[year]
	if config['invert']:
		image = cv2.bitwise_not(image)
	if config['blackwhite']:
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		thres, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # values can be adjusted
		image = (image)
	if config['thicken_font'][0]:
		if not (config['invert']):
			image = cv2.bitwise_not(image)
		kernel = np.ones((config['thicken_font'][1],config['thicken_font'][1]), np.uint8)
		image = cv2.dilate(image, kernel, iterations=config['thicken_font'][2])
	if config['thin_font'][0]:
		if not (config['invert']):
			image = cv2.bitwise_not(image)
		kernel = np.ones((config['thin_font'][1],config['thin_font'][1]), np.uint8)
		image = cv2.dilate(image, kernel, iterations=config['thin_font'][2])
	if config['deskew']:
		angle = getSkewAngle(image)
		image = rotateImage(image, -1.0 * angle)
	if config['noise_removal']:
		kernel = np.ones((config['noise_removal'][1],config['noise_removal'][1]), np.uint8)
		image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
		image = cv2.medianBlur(image, config['noise_removal'][2])
	return image