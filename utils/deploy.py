import torch

import cml.models_v1 as models

model = torch.load('torch_model.pth')

@models.cml_model
def predict():
    img = load_img('/home/cdsw/images/bird.png' , target_size = (32 , 32))
    img = img_to_array(img)
    img = img.reshape(1 , 32 ,32 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)

    dict_result = {}
    for i in range(10):
        dict_result[result[0][i]] = classes[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
    
    prob_result = []
    for i in range(3):
        prob_result.append((prob[i]*100).round(2))

    return prob_result