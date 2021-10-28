import numpy as np

class1 = np.random.randint(0,100,size=(50,3))
class2 = np.random.randint(0,100,size=(50,3))
class3 = np.random.randint(0,100,size=(50,3))
class4 = np.random.randint(0,100,size=(50,3))
class5 = np.random.randint(0,100,size=(50,3))
class6 = np.random.randint(0,100,size=(50,3))


classtoal = np.concatenate([class1,class2,class3,class4,class6,class5])

sec = np.random.randint(0,2,size=(50*6,1))

class_data = np.concatenate([classtoal,sec],axis=1)

min_score = classtoal.min(axis=0)
max_score = classtoal.max(axis=0)
avg_score = classtoal.mean(axis=0)
medium_score = np.median(classtoal)
std = np.std(classtoal)