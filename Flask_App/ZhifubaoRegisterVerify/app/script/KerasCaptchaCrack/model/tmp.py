import base64
import io


from PIL import Image
img_file = r'C:\Users\YongHu\Desktop\TMP\data\train\2ABU_abeb7912-d5af-11e7-ae6a-dc4a3e8b7c67.png'
f = open(img_file, 'rb')
img_data = f.read()

img_base64 = base64.encodebytes(img_data).decode()

img_d = base64.b64decode(img_base64)

img_like = io.BytesIO(img_d)

# print(img_d)
#
img = Image.open(img_like)
img.show()
#
# img = img.convert("RGB")
# img.show()

