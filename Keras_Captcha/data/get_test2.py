import os
import shutil

old_folder = r'C:\Users\YongHu\Desktop\TMP\data\train'

new_folder = r'C:\Users\YongHu\Desktop\imgs\test'

old_imgs = set(os.listdir(old_folder))

new_imgs = set(os.listdir(new_folder))

nn = new_imgs - old_imgs


nn_folder = r'C:\Users\YongHu\Desktop\TMP\data\test2'
for n in nn:
    shutil.copy(os.path.join(new_folder, n), os.path.join(nn_folder, n))
    print(n, ' has been copied to train data')



