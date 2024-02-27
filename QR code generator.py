#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install qrcode  


# In[7]:


# importing the qrcode module  
import qrcode  
# creating a QRCode object  
obj_qr = qrcode.QRCode(  
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)  
# using the add_data() function  
obj_qr.add_data("python")  
# using the make() function  
obj_qr.make(fit = True)  
# using the make_image() function  
qr_img = obj_qr.make_image(fill_color = "cyan", back_color = "black")  
# saving the QR code image  
qr_img.save("qr-img1.png")  


# In[6]:


# importing the qrcode library  
import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make("Welcome")  
# saving the image file  
qr_img.save("qr-img.jpg")  


# In[ ]:




