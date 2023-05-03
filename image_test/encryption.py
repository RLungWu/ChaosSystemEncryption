from PIL import Image
import numpy as np
import math
import random

def encry():
    #load Image
    image = Image.open("./Image/image2.jpg")
    image_array = np.array(image)

    
    first = random.randint(0,255)
    second = random.randint(0,255)
    if first > second:
        first,second = second,first
    method = 0

    #Tent 映射
    x = [first, second, method]

    #消除初始影響
    x.append(x[0] / x[1])
    w = image_array.shape[0]
    h = image_array.shape[1]
    size = w * (h+1) * 3

    print(len(x))
    print(size)

    while len(x) != size:
        xn = x[-1]
        xn = round(1-2 * abs(xn - 0.5), 10)
        x.append(xn)
        

    chaos_scaled = np.round(np.array(x) * 255).astype(int)

    chaos_scaled_3D = chaos_scaled.reshape((image_array.shape[0], image_array.shape[1] + 1,3))
    
    #使用xor
    c = []
    for i in range(image_array.shape[0]):
        arr1 = []
        for j in range(image_array.shape[1]):
            arr2 = []
            for k in range(image_array.shape[2]):
                temp = image_array[i][j][k] ^ chaos_scaled_3D[i][j][k]
            
                arr2.append(temp)
        #print(arr2)
            arr1.append(arr2)
        c.append(arr1)
    
    #輸出圖片
    data = np.array(c)
    image_enc = Image.fromarray(data.astype('uint8'), mode='RGB')
    image_enc.save('./Image/Encrypted_image2.png')

    








