# Tech Note 16-06: Integrating Facial Detection and Recognition in 4D - Revised

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** May 26, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77536
**Download:** https://kb.4d.com/DLTN/TN/2016/16-06_FacialRecognition_R1.zip

## Proposition
This note demonstrates integrating face detection (via Haar Cascade classifiers) and face recognition (via the LBPH algorithm) into 4D applications by calling OpenCV through Python, exposing simplified PY_DETECT_FACES, PY_CROP_FACES, and PY_CREATE_RECOGNIZER functions for use from 4D code.

## Key Points
- **Haar Cascade face detection:** explains Haar-like features, AdaBoost-based feature selection, and cascading classifiers used to locate faces in images.
- **OpenCV Python API coverage:** documents CascadeClassifier and its detectMultiscale method for face detection.
- **LBPH face recognition:** covers Local Binary Patterns Histogram-based recognition, including training set preparation and normalization.
- **4D-to-Python bridge:** demonstrates running Python functions directly from 4D code.
- **Three ready-to-use functions:** PY_DETECT_FACES, PY_CROP_FACES, and PY_CREATE_RECOGNIZER wrap the underlying OpenCV calls.
- **Demo database included** showing available functions with example parameter usage.

## Featured Technology
- Python
- OpenCV (Haar Cascade classifiers, LBPH FaceRecognizer)
- 4D-to-Python interoperability bridge
- Computer vision / machine learning basics

## Best Practices Highlighted
1. Normalize training images before feeding them into a recognizer for more reliable results.
2. Wrap external library calls (OpenCV/Python) behind simple, well-documented 4D-callable functions.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Deprecated

Haar Cascade detection and LBPH recognition were reasonably capable techniques in 2016 but are now considered legacy computer-vision approaches: modern face detection/recognition overwhelmingly uses deep-learning models (e.g., OpenCV's DNN module, dlib, or dedicated services), which are substantially more accurate, especially across lighting, angle, and demographic variation. The general pattern of calling out to Python from 4D for specialized libraries remains valid and is even easier today, but the specific OpenCV APIs shown are dated and the accuracy/reliability bar has moved significantly.
