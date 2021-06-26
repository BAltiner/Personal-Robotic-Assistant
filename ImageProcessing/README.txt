bg.txt contains each negative pictures paths
pos.txt contains:img, num objects, start point, rect coordinates

!
Negative images should be larger than positives.Like 100x100 for negatives, 50x50 for positives.
Negative dataset is taken from      : https://www.kaggle.com/muhammadkhalid/negative-images
Eye detection cascade from          :https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
Face detection cascade from         :https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

utils:
https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html
https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html
http://note.sonots.com/SciSoftware/haartraining.html#t1a1f262
ImageProcessing\FaceRecognition\DefaultFaceDetect\haarcascade_frontalface_default.xml used for creation positive dataset (if face detected:	take a picture)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

vec file creation:
command>>opencv_createsamples.exe -vec pos.vec -bg bg.txt -num 459 -info pos.dat -w 24 -h 24
>>
Info file name: pos.dat
Img file name: (NULL)
Vec file name: pos.vec
BG  file name: bg.txt
Num: 459
BG color: 0
BG threshold: 80
Invert: FALSE
Max intensity deviation: 40
Max x angle: 1.1
Max y angle: 1.1
Max z angle: 0.5
Show samples: FALSE
Width: 24
Height: 24
Max Scale: -1
RNG Seed: 12345
Create training samples from images collection...
Done. Created 459 samples

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

xml cascade creation: (cmd output)
C:\Users\beste\Desktop\EngiDesign\ImageProcessing\FaceRecognition>opencv_traincascade.exe -data Classiffiers -vec pos.vec -bg bg.txt -numPos 400 -numNeg 200 -numStage 12 -featureType HAAR -minHitRate 0.999 -maxFalseAlarmRate 0.5 -w 24 -h 24
PARAMETERS:
cascadeDirName: Classiffiers
vecFileName: pos.vec
bgFileName: bg.txt
numPos: 400
numNeg: 200
numStages: 20
precalcValBufSize[Mb] : 1024
precalcIdxBufSize[Mb] : 1024
acceptanceRatioBreakValue : -1
stageType: BOOST
featureType: HAAR
sampleWidth: 24
sampleHeight: 24
boostType: GAB
minHitRate: 0.999
maxFalseAlarmRate: 0.5
weightTrimRate: 0.95
maxDepth: 1
maxWeakCount: 100
mode: BASIC
Number of unique features given windowSize [24,24] : 162336

===== TRAINING 0-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 1
Precalculation time: 0.354
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|     0.08|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 1 seconds.

===== TRAINING 1-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.220022
Precalculation time: 0.368
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|     0.07|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 2 seconds.

===== TRAINING 2-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.0304553
Precalculation time: 0.36
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|     0.08|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 3 seconds.

===== TRAINING 3-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.00556948
Precalculation time: 0.369
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|     0.22|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 4 seconds.

===== TRAINING 4-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.00156107
Precalculation time: 0.361
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|     0.18|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 5 seconds.

===== TRAINING 5-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.000670461
Precalculation time: 0.364
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|     0.42|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 7 seconds.

===== TRAINING 6-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.000567418
Precalculation time: 0.376
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|     0.74|
+----+---------+---------+
|   3|        1|    0.425|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 10 seconds.

===== TRAINING 7-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 0.000224369
Precalculation time: 0.362
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|    0.595|
+----+---------+---------+
|   3|        1|    0.345|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 15 seconds.

===== TRAINING 8-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 8.72862e-05
Precalculation time: 0.361
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|    0.655|
+----+---------+---------+
|   3|        1|     0.38|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 21 seconds.

===== TRAINING 9-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 4.22879e-05
Precalculation time: 0.366
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|     0.71|
+----+---------+---------+
|   3|        1|    0.485|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 33 seconds.

===== TRAINING 10-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 2.35589e-05
Precalculation time: 0.365
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|    0.775|
+----+---------+---------+
|   3|        1|    0.775|
+----+---------+---------+
|   4|        1|     0.48|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 0 minutes 52 seconds.

===== TRAINING 11-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 1.41679e-05
Precalculation time: 0.359
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|     0.43|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 1 minutes 20 seconds.

===== TRAINING 12-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    200 : 6.35665e-06
Precalculation time: 0.36
+----+---------+---------+
|  N |    HR   |    FA   |
+----+---------+---------+
|   1|        1|        1|
+----+---------+---------+
|   2|        1|    0.665|
+----+---------+---------+
|   3|        1|     0.39|
+----+---------+---------+
END>
Training until now has taken 0 days 0 hours 2 minutes 21 seconds.

===== TRAINING 13-stage =====
<BEGIN
POS count : consumed   400 : 400
NEG count : acceptanceRatio    1 : 4.76837e-07
Required leaf false alarm rate achieved. Branch training terminated.


Important! Required leaf false alarm rate achieved. Branch training terminated. -> It is not an error.(It means training stages are enough and face recognition can be done with created cascade.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

im gonna add time info at the end...
