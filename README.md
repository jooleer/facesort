# FaceSort

#### Video Demo: https://youtu.be/_cZjR3e6i68

## Description:

FaceSort uses python with a combination of the Deepface (link) and RetinaFace (link) libraries to detect faces from a collection of images and afterwards sorts them by recognizing those faces and arranges the images in folders for each unique face found.
<br/><br/>

# Installation:

Making sure the packages from `requirements.txt` are installed, the easiest way is to `git clone https://github.com/joleer/facesort` and use `pip install -r requirements.txt`

Alternatively, you can also manually install the packages:

```
pip install deepface
pip install retinaface
pip install matplotlib.pyplot
pip install opencv-python
```

and afterwards use `git clone https://github.com/joleer/facesort` or manually download and extract the repository.  
<br/>

# Usage:

**Supported image filetypes are:** jpg, jpeg, png and bmp

Place facesort.py one folder above your `./images` folder or set a custom folder in _facesort.py_ under _images_directory_

Run by using `python facesort.py`

The application will start off by scanning all images in the folder and making a list of all the unique faces found.
After all images have been checked for faces, the original images will be copied into new folders with each folder being tied to one person's face.

After the application is done all orignal images will be untouched and you can find your sorted images and person folders in the `./facesort/` folder.

**The first time running this software, one or several pre-trained weight files might be automatically downloaded.**

You can also manually download these files here: [DeepFace Models Pre-Trained Weights](https://github.com/serengil/deepface_models/releases)

<br/>

# Sources:

## Main libraries used:

[DeepFace](https://github.com/serengil/deepface)  
[RetinaFace](https://github.com/serengil/retinaface)
<br/><br/>
**RetinaFace** is based on the _RetinaFace: Single-stage Dense Face Localisation in the Wild_ research paper by Jiankang Deng, Jia Guo, Yuxiang Zhou, Jinke Yu, Irene Kotsia and Stefanos Zafeiriou.  
More information on the paper can be found here https://arxiv.org/abs/1905.00641 (paper available in pdf format here: https://arxiv.org/pdf/1905.00641.pdf)
<br/><br/>

### Images used for the project's testing purposes seen in the explanation video were gathered from the following sources:

- https://www.buzzfeed.com/
- https://www.insider.com/
- https://www.tatlerasia.com/
- https://reelrundown.com/
- https://www.irishexaminer.com/
- https://www.teenvogue.com/
- https://www.oprahdaily.com/
- https://www.nottinghampost.com/

<br/><br/>

# Final notes:

FaceSort is not perfect and might not recognize some faces, erroneously recognize someone as another person, detect people in the background you didn't intend to get sorted or not recognize a face from pictures that may seem similar to our human eyes.  
For the best results, use images where faces are clearly visable. Blurry faces or images, changes in facial hair, age or other factors can influence the recognition algorythm accuracy.  
<br/>
As technology and models advance face recognition will get faster and more precise, the underlying structure of this software is based on models created by processing millions of images and have in some cases surpassed humans face recognition.  
FaceSort by default uses the VGG-Face model (link: http://www.robots.ox.ac.uk/~vgg/software/vgg_face/) which is licensed under the Creative Commons Attribution License (link: https://creativecommons.org/licenses/by-nc/4.0/). Other models (Facenet, OpenFace, DeepFace, DeepID, ArcFace, Dlib and SFace) that you are able to use with this software may have different licenses. Make sure to check the license type of the model you intend to use and that it fits your purpose.  
<br/>
If you are interested in more information about the technologies used by FaceSort check out **DeepFace** on [GitHub](https://github.com/serengil/deepface) and [Wikipedia](https://en.wikipedia.org/wiki/DeepFace), **RetinaFace** on [GitHub](), **Face Detection** on [Wikipedia](https://en.wikipedia.org/wiki/Face_detection) and **Facial Recognition** on [Wikipedia](https://en.wikipedia.org/wiki/Facial_recognition_system)  
<br/>
_This software was created for educational purposes for my final project for CS50 and is licensed under the [MIT License](https://github.com/jooleer/facesort/blob/main/LICENSE)._
