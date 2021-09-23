
# coding: utf-8

# In[ ]:


Main()


# In[ ]:


Main.iterators


# In[ ]:


rubik


# In[1]:


import numpy as np
import math
import matplotlib.image as mpimg



# In[2]:


def Main():
    #Figurative main function , the starting point
    
    global rubik , edgelen , img , edgelen , imgnew
    
    print('Rubeka V 1.0 -- Author : Saifuddin M Raja     ')
    address=input('Please enter the name of the image file   ')
    
    img = mpimg.imread(address )
    print(type(img))
    imlen = img.shape
    print(imlen)
    imlenx = imlen[0]
    imleny = imlen[1]
    edgelen = math.ceil((imlenx * imleny)**(1/3))
    rubik = np.zeros((edgelen , edgelen , edgelen))
    imgnew = np.zeros((imlenx,imleny))
    ii =0
    ji =0
    
    
    for x in range(0,edgelen):
        for y in range(0,edgelen):
            for z in range(0,edgelen):
                if (ii == imlenx):
                    ji = ji + 1
                    ii = 0
                try :
                    rubik[x,y,z] = img[ii , ji]
                except:
                    print('error',ii , ji,end='*')
                ii = ii + 1
                Main.iterators=[ii,ji]
    
                    
            
        
    
    
    eord=input('Encrypt or Decrypt ?...(type 1 or 2)  ')
    
    #switch case construct here
    if eord == '1' :
            Encrypt()
            print('Encryption Performed')
            
    elif eord == '2' :
            Decrypt()
            print('Decryption Performed')
    
    
    
    
    print('control returned from e/d to rubeka')
    print('post processing started')
    
    ii =0
    ji =0
    
    
    for x in range(0,edgelen):
        for y in range(0,edgelen):
            for z in range(0,edgelen):
                if (ii == imlenx):
                    ji = ji + 1
                    ii = 0
                try :
                    imgnew[ii , ji]=rubik[x,y,z]
                except:
                    print('error',ii , ji,end='*')
                ii = ii + 1
                Main.iterators=[ii,ji]
    
                
            
        
    
    
    print('post processing ed')
    print('New image creation started')
    mpimg.imsave(('new'+address),imgnew)
    print('New image creation complete : newlena.bmp , Happy Cryptography !! ')


# In[3]:


def Encrypt():
    #Summary
    
    global edgelen
    
    ekey= input('Encryption:   enter 7 digit passkey [x x x x x x x]:  ')
    shfl_seq = int(ekey[0])
    xturns= int(ekey[1])
    xstyle= int(ekey[2])#style variables have to do with mat file PatternCommand
    yturns= int(ekey[3])
    ystyle= int(ekey[4])
    zturns= int(ekey[5])
    zstyle= int(ekey[6])
    
    if shfl_seq == 0:
            #style is XYZ
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 3 , zturns , zstyle)
            #call xrot for Xturns also parse to it Xtsyle
            #then do for Y
            #then do for Z
    elif shfl_seq == 1:
            #style is XZY
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 2 , yturns , ystyle)
    elif shfl_seq == 2:
            #style is YXZ
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , zturns , zstyle)
    elif shfl_seq == 3:
            #style is YZX
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 1 , xturns , xstyle)  
    elif shfl_seq == 4:
            #style is ZXY
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , yturns , ystyle)
    elif shfl_seq == 5:
            #style is ZYX
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , xturns , xstyle)     
    elif shfl_seq == 6:
            #style is -XYZ
            PaternCommand( 1 , (xturns *-1) , xstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 3 , zturns , zstyle)
    elif shfl_seq == 7:
            #style is -YXZ
            PaternCommand( 2 , (yturns *-1) , ystyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , zturns , zstyle)
    elif shfl_seq == 8:
            #style is -ZXY
            PaternCommand( 3 , (zturns *-1) , zstyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , yturns , ystyle)
    elif shfl_seq == 9:
            #style is -X-Y-Z
            PaternCommand( 1 , (xturns *-1) , xstyle)
            PaternCommand( 2 , (yturns *-1) , ystyle)
            PaternCommand( 3 , (zturns *-1) , zstyle)


# In[4]:


def Decrypt():
    #Summary
    
    global edgelen
    
    ekey= input ('Decryption:   enter 7 digit passkey [x x x x x x x]:  ')
    shfl_seq = int(ekey[0])
    xturns= int(ekey[1] *-1)
    xstyle= int(ekey[2])#style variables have to do with mat file PatternCommand
    yturns= int(ekey[3] *-1)
    ystyle= int(ekey[4])
    zturns= int(ekey[5] *-1)
    zstyle= int(ekey[6])
    
    if shfl_seq == 0:
            #style is XYZ
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , xturns , xstyle)
            
    elif shfl_seq == 1:
            #style is XZY
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 1 , xturns , xstyle)
            
    elif shfl_seq == 2:
            #style is YXZ
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , yturns , ystyle)
            
    elif shfl_seq == 3:
            #style is YZX
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 2 , yturns , ystyle)
                  
    elif shfl_seq == 4:
            #style is ZXY
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , zturns , zstyle)
            
    elif shfl_seq == 5:
            #style is ZYX
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 3 , zturns , zstyle)
                    
    elif shfl_seq == 6:
            #style is -XYZ
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , (xturns *-1) , xstyle)
            
    elif shfl_seq == 7:
            #style is -YXZ
            PaternCommand( 3 , zturns , zstyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 2 , (yturns *-1) , ystyle)
            
    elif shfl_seq == 8:
            #style is -ZXY
            PaternCommand( 2 , yturns , ystyle)
            PaternCommand( 1 , xturns , xstyle)
            PaternCommand( 3 , (zturns *-1) , zstyle)
            
    elif shfl_seq == 9 :
            #style is -X-Y-Z
            PaternCommand( 3 , (zturns *-1) , zstyle)
            PaternCommand( 2 , (yturns *-1) , ystyle)
            PaternCommand( 1 , (xturns *-1) , xstyle)
            


# In[5]:


def  PaternCommand( axis , turns , style):
    #  this function simply takes 3 inputs :
    # plane... x,y,z
    # no of turns
    # style of encryption
    
    global edgelen
    
    if style == 0:
            #style is fix-spin
            for i in range(1,edgelen):
                if( i%2 == 1):
                    spinpos = i 
                    XYZDec( axis , turns , spinpos)
                
            
            
    elif style == 1:
            #style is fix-fix-spin
            for i in range(1,edgelen):
                if( i%3 == 0):
                    spinpos = i -1 
                    XYZDec( axis , turns , spinpos)
                
            
    elif style == 2:
            #style is fix-fix-spin-spin
            for i in range(1,edgelen):
                if( i%4 == 0):
                    spinpos = i -2 
                    XYZDec( axis , turns , spinpos)
                    XYZDec( axis , turns , spinpos +1)
                
            
    elif style == 3:
            #style is fix-fix-antispin
            for i in range(1,edgelen):
                if( i%3 == 0):
                    spinpos = i -1 
                    XYZDec( axis , (turns * -1) , spinpos)
                
            
    elif style == 4:
            #style is fix-fix-antispin-antispin
            for i in range(1,edgelen):
                if( i%4 == 0):
                    spinpos = i -2 
                    XYZDec( axis , (turns * -1) , spinpos)
                    XYZDec( axis , (turns * -1) , spinpos +1)
                
            
    elif style == 5:
            #style is fix-spin-fix-antispin
            for i in range(1,edgelen):
                if( i%4 == 0):
                    spinpos = i -3 
                    XYZDec( axis , turns , spinpos)
                    XYZDec( axis , (turns * -1) , spinpos +2)
                
            
    elif style == 6:
            #style is fix-antispin-fix-spin
            for i in range(1,edgelen):
                if( i%4 == 0):
                    spinpos = i -3 
                    XYZDec( axis , (turns * -1) , spinpos)
                    XYZDec( axis , turns , spinpos +2)
                
            
    elif style == 7:
            #style is fix-spin-antispin-fix
            for i in range(1,edgelen):
                if( i%4 == 0):
                    spinpos = i -3
                    XYZDec( axis , turns , spinpos)
                    XYZDec( axis , (turns * -1) , spinpos +2)
                
            
    elif style == 8:
            #style is fix-spin-antispin-spin-fix
            for i in range(1,edgelen):
                if( i%5 == 0):
                    spinpos = i -4
                    XYZDec( axis , turns , spinpos)
                    XYZDec( axis , (turns * -1) , spinpos +1)
                    XYZDec( axis , turns , spinpos +2)
                
            
    elif style == 9:
            #style is fix-antispin-spin-antispin-fix
            for i in range(1,edgelen):
                if( i%5 == 0):
                    spinpos = i -4
                    XYZDec( axis , (turns * -1) , spinpos)
                    XYZDec( axis , turns , spinpos +1)
                    XYZDec( axis , (turns * -1) , spinpos +2)
                
            


# In[6]:


def XYZDec( axis , turns , spinpos):
    global rubik , edgelen , rubik2
    #decides which axis mainpulaiton to go with 
    
    if axis == 1 :
            XRot1(turns , spinpos )
    elif axis == 2 :
            YRot1(turns , spinpos )
    elif axis == 3 :
            ZRot1(turns , spinpos )


# In[7]:


def XRot1( xturns , xa ):
    #XRot rotates every odd plane for Xturns
    global rubik , edgelen
    #tempslice = np.zeros((edgelen , edgelen))
    tempslice = rubik[xa,:,:]
    tempslice = np.rot90(tempslice , xturns)
    rubik[xa,:,:] = tempslice
        


# In[8]:


def YRot1( yturns , ya ):
    #YRot rotates every odd plane for Y turns
    global rubik , edgelen
    #tempslice = np.zeros((edgelen , edgelen))
    tempslice = rubik[:,ya,:]
    tempslice = np.rot90(tempslice , yturns)
    rubik[:,ya,:] = tempslice
        


# In[9]:


def  ZRot1( zturns , za ):
    #ZRot rotates every odd plane for Zturns
    global rubik , edgelen
    #tempslice = np.zeros((edgelen , edgelen))
    tempslice = rubik[:,:,za]  
    tempslice = np.rot90(tempslice , zturns)
    rubik[:,:,za] = tempslice
    

