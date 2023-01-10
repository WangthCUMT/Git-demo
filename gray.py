# 开发时间: 2022/10/28 15:01
import numpy as np
import cv2
import skimage.feature
import os
import pandas as pd
path = 'C:/Users/MSI-NB/Desktop/bp network'
ENTls = []
HOMO = []
CON = []
ENE = []
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.tif':
        I = cv2.imread(path+'/'+filename, 0)
        result = skimage.feature.graycomatrix(I, [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256)
        Entropy = skimage.feature.graycoprops(result, 'entropy')
        ENTls.append(np.mean(Entropy))
        Homogeneity = skimage.feature.graycoprops(result, 'homogeneity')
        HOMO.append(np.mean(Homogeneity))
        Contrast = skimage.feature.graycoprops(result, 'contrast')
        CON.append(np.mean(Contrast))
        Energy = skimage.feature.graycoprops(result, 'energy')
        ENE.append(np.mean(Energy))
df1 = pd.DataFrame(ENTls)
df2 = pd.DataFrame(HOMO)
df3 = pd.DataFrame(CON)
df4 = pd.DataFrame(ENE)
with pd.ExcelWriter('57train.xlsx') as writer:
    df1.to_excel(writer, sheet_name='熵',index=False)
    df2.to_excel(writer, sheet_name='同质度', index=False)
    df3.to_excel(writer, sheet_name='对比度', index=False)
    df4.to_excel(writer, sheet_name='能量', index=False)
