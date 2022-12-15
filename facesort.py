from deepface import DeepFace
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import shutil
import sys
import cv2
import os

# variables and paths declaration
# work paths
work_path = './facesort/'
faces_directory = './facesort/faces/'
images_directory = './images/'

# specify which image formats are supported
image_types = ('.jpg', '.jpeg', '.png', '.bmp')

# temporary variable name for face comparison
temp_face = 'temp_face.png'

# individual face image variables
person_face_prefix = 'person_'
person_face_filetype = '.png'

# options for DeepFace verification models and metrics
deepface_models = ['VGG-Face', 'Facenet', 'Facenet512', 'OpenFace', 'DeepFace', 'DeepID', 'ArcFace', 'Dlib', 'SFace',]
deepface_metrics = ['cosine', 'euclidean', 'euclidean_l2']

# declaration of variables used for initial image discovery
image_list = []

# declaration of variables for face detection
people_list = []
PersonID = 0


# get argument(s) if they were provided
arg = ''
if len(sys.argv) > 1:
    arg = sys.argv[1]

print("\nFaceSort - https://github.com/jooleer/facesort/", "\n")

# check if paths already exist
# create them if they don't
if not os.path.exists(work_path):
    os.mkdir(work_path)

if not os.path.exists(faces_directory):
    os.mkdir(faces_directory)

else:
    # check if faces_directory is empty
    # if not, warn the user about overwriting previous data/images and exit
    dir = os.listdir(faces_directory)
    if len(dir) != 0 and arg != '-o':
        print("To avoid losing or overwriting data please make sure the", work_path, "and", faces_directory, "are empty of any data you don't want to lose.")
        print("Use \"python facesort.py -o\" to allow overwriting files. (Not recommended)")
        print("Alternatively, you can change the path variables in facesort.py")
        exit(1)

    # if user still has files but uses -o parameter we continue anyway
    elif len(dir) != 0 and arg == '-o':
        print("Directories were not empty but overwrite command was used.")



# declaration of functions

# search directory provided in argument for images
# make a list (append image_list) of all images found
def scan_images(directory="./"):
    for folder_image in os.listdir(directory):
        if folder_image.endswith(image_types):
            image_list.append(folder_image)

    # if no images are found in the folder, notify user and exit
    if len(image_list) == 0:
        print("No images were found in the provided directory: ",directory)
        exit(2)
    
    # print out the amount of images found 
    print("Found", len(image_list), "images in", faces_directory)


# check faces folder if face already exists
def check_face(image, directory=faces_directory, face_to_check=temp_face):
    
    # clear people_list to start with an empty list
    people_list.clear()

    # use PersonID as a global variable to use it across multiple functions
    global PersonID

    # make a list of all faces found in (faces) directory
    for face in os.listdir(directory):
        if face.endswith(image_types):
            people_list.append(face)

    # call match_face to check if face_to_check is found in directory
    copy_face = match_face(image, directory, face_to_check, people_list)
    
    # if face_to_check was not found in the faces_directory, create a new image and tie it to a PersonID
    if copy_face:
        # add image in the list tied to their PersonID
        list_of_faces[PersonID].append(image)

        old_name = (directory + face_to_check)
        new_name = (directory + person_face_prefix + str(PersonID) + person_face_filetype)

        # person not found in folder yet, add them to person list and copy temp image with their PersonID
        shutil.copyfile(old_name, new_name)
        PersonID = int(PersonID) + 1

    # remove all elements from people_list
    people_list.clear()


# check directory in parameter to see if face_to_check is already in it
def match_face(image, directory, face_to_check, list_of_people=people_list):

    for person in list_of_people:

        # variables for DeepFace verification
        img1_path = directory + face_to_check
        img2_path = directory + person
        verify = DeepFace.verify(img1_path, img2_path, enforce_detection=False, model_name=deepface_models[0], distance_metric=deepface_metrics[0], align=True)

        # check result of DeepFace verification
        if verify['verified'] and face_to_check != person:
            # face already exists, add the current image to the list of this persons ID
            # extract PersonID from the face that face_to_check matched with
            temp_id = str(person).removeprefix(person_face_prefix)
            temp_id = temp_id.removesuffix(person_face_filetype)

            # add image to PersonID's list in list_of_faces
            list_of_faces[int(temp_id)].append(image)

            # return False if matching face was found
            return False

    # return True if no matching faces were found    
    return True


# extract faces from images in image_list
def extract_faces():
    # loop through all images found in the folder
    for image in image_list:
        # use RetinaFace to get all faces in the image
        faces = RetinaFace.extract_faces(images_directory + image, align = True, allow_upscaling = False)

        # list of faces found in image
        print(len(faces), "face(s) were found in image: ", image)

        # loop through all faces in the image
        for face in faces:
            # save temporary temp_face image to faces_directory
            plt.imsave(fname = faces_directory + temp_face, format='png', arr=face)

            # call check_face function to verify and sort faces
            check_face(image, faces_directory, temp_face)


# sort images into individual PersonID's folders
def sort_images():
    # loop through all individual gathered faces listed in PersonID
    for individual in range(PersonID):
        # path variable for each PersonID's individual folder
        individual_path = work_path + person_face_prefix + str(individual) + '/'
        # create PersonID folder if it doesn't exist yet
        if not os.path.exists(individual_path):
            os.mkdir(individual_path)

        # copy PersonID's face to their folder
        base_face = faces_directory + person_face_prefix + str(individual) + person_face_filetype
        folder_face = individual_path + '_' + person_face_prefix + str(individual) + person_face_filetype
        shutil.copyfile(base_face, folder_face)
        
        # loop through all pictures tied to the PersonID's list
        for pictures in list_of_faces[int(individual)]:
            # variables to copy images for each person
            copy_from_path = images_directory + pictures
            copy_to_path = individual_path + pictures

            # copy each image to the PersonID's folder
            shutil.copyfile(copy_from_path, copy_to_path)


print("\nDepending on your system and amount of images this process may take a while.\n")

# scan folder for all images
scan_images(images_directory)

# every image that matches a PersonID will be added to the list for sorting to individual folders
list_of_faces = [[] for x in range(len(image_list)*len(image_list))]

# extract faces from images
print("Extracting faces..")
extract_faces()

# sort faces to folders
print("\nSorting images..")
sort_images()

# delete temporary image face file
if (os.path.isfile(faces_directory+temp_face)):
    os.remove(faces_directory+temp_face)


print("Process completed successfully.")
print(len(image_list),"image(s) were found and sorted into folders by",int(PersonID)-1,"unique faces.")
print("\nThank you for using FaceSort.")
print("https://github.com/jooleer/facesort/", "\n")
exit(0)
