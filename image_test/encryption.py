from PIL import Image
import numpy as np
import math

def encry():
    #load Image
    image = Image.open("image2.jpg")
    image_array = np.array(image)

    #Tent 映射
    x0 = 0.234567
    x = [x0]

    #消除初始影響
    for i in range(99):
        xn = x[-1]
        xn = round(1 - 2 * abs(xn - 0.5),10)
        x.append(xn)
    chaos = [x[-1]]

    for i in range(image_array.shape[0] * image_array.shape[1] * 3 -1):
        xn = chaos[-1]
        xn = round(1 - 2 * abs(xn-0.5),10)
        chaos.append(xn)

    chaos_scaled = np.round(np.array(chaos) * 255).astype(int)

    chaos_scaled_3D = chaos_scaled.reshape((image_array.shape[0], image_array.shape[1],3))
    
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
    image_enc.save('Encrypted_image2.png')

    








