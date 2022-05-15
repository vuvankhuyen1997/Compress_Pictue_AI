# Compress_Pictue_AI

An application which can compress an image less than almost 1/3 of original size by using K Means.

REQUIREMENT: This application needs

  1. Python3
  2. $pip install matplotlib
  3. $pip install scikit-learn
  4. $pip install numpy

RUN THE APPLICATION: 
  
  1. Run: $python clean_data.py
    To clean all setting to original. If first time using, no need.
  2. Download picture which you want to compress and put it in the same folder (remember to set the picture to .jpg type).
  3. Open test_cluster.py file, change the name of picture in line 9 (img = plt.imread("....jpg")).
  4. Run: $python test_cluster.py
    The chart will be appear, analysis and choose the cluster you want base on elbow.
  5. Open main.py file, change the name of picture in line 9 (img = plt.imread("....jpg")). Then change the cluster you choose in step 4 in line 17 (n_clusters=...)
  6. Run: $python main.py
    The compress picture will be appear after the process.
