%Figurative main function , the starting point


display('Rubeka V 0.7 ------ Author : Saifuddin M Raja     ');
address=input('Please enter the name of the image file');
img = imread(address);
imlen = size(img)
imlenx = imlen(1);
imleny = imlen(2);
len_stream = ceil(nthroot((imlenx * imleny) , 3))
%display('empty rubik generated');
ii =0;
ji =1;
for x= 1:len_stream
    for y= 1:len_stream
        for z= 1:len_stream
            while (ii < imlenx)&&(ji < imleny)
            ii = ii + 1;
            if (ii == imlen)
                ji = ji + 1;
                ii = 1;
                
            end
            tempa = img(ii , ji);
            rubik(x,y,z) = tempa;
            end
        end
    end
end
display('matrix filling complete');

eord=input('Encrypt or Decrypt ?...(type 1 or 2)');

%switch case construct here
switch eord 
    case 1
        rubik=Encrypt1(rubik , len_stream);
        display('Encryption Chosen');
    case 2
        rubik=Decrypt1(rubik , len_stream);
        display('Decryption Chosen');

end


display('control returned from e/d to rubeka');
display('post processing started');

ii =0;
ji =1;

for x=1:len_stream
    for y=1:len_stream
        for z=1:len_stream
            while (ii < imlenx)&&(ji < imleny)
            ii = ii + 1;
            if (ii == imlen)
                ji = ji + 1;
                ii = 1;
            end
            temps = rubik(x,y,z);
            imgnew(ii , ji) = temps;
            end
        end
    end
end

display('post processing ended');
display('New image creation started');
imwrite(uint8(imgnew),'newlena.bmp','bmp');
display('New image creation complete : newlena.bmp , Happy Cryptography !! ');


