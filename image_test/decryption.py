from PIL import Image
import numpy as np
import math

def decry():
    #load Image
    image = Image.open("./Image/Encrypted_image2.png")
    image_array = np.array(image)

    #Tent 映射
    first = image_array[0][0][0]
    second = image_array[0][0][1]
    type = image_array[0][0][2]
    x = [first, second, type, first/second]
    print('x:')
    print(x)
    #消除初始影響
    w = image_array.shape[0]
    h = image_array.shape[1]
    size = w * h * 3
    

    #x0 = first / second
    while len(x) != size:
        xn = x[-1]
        xn = round(1 - 2 * abs(xn - 0.5), 10)
        x.append(xn)

    chaos_scaled = np.round(np.array(x) * 255).astype(int)

    chaos_scaled_3D = chaos_scaled.reshape((image_array.shape[0], image_array.shape[1],3))
    
    #使用xor
    c = []
    for i in range(image_array.shape[0]):
        arr1 = []
        if i == 0:
            for j in range(image_array.shape[1]):
                arr2 = []
                for k in range(image_array.shape[2]):
                    temp = chaos_scaled_3D[i][j][k] ^ image_array[i][j][k]
                    arr2.append(temp)
                arr1.append(arr2)
        else:
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
    image_enc.save('./Image/Decrypted_image2.png')

    return chaos_scaled_3D








