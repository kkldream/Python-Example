opencv_createsamples -vec pos.vec -info pos.txt -bg neg.txt -w 50 -h 50

opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 200 -numNeg 600 -numStages 15 -featureType HAAR -w 50 -h 50 -minHitRate 0.9999 -maxFalseAlarmRate 0.5 -precalcValBufSize 2000 -precalcIdxBufSize 2000 -mem 3500

opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 200 -numNeg 600 -numStages 20 -featureType HAAR -w 50 -h 50 -minHitRate 0.9999 -maxFalseAlarmRate 0.5 -precalcValBufSize 2000 -precalcIdxBufSize 2000 -mem 3500

