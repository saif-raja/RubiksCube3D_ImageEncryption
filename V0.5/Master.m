% fucked up kichadi of all functions together not my idea
fprintf('Rubeka V 0.5');
stream_string=input('Please enter the text');
global len_stream;
len_stream = ceil(nthroot(length(stream_string) , 3));
rubik= zeros(len_stream,len_stream,len_stream);
for x=1:len_stream
    for y=1:len_stream
        for z=1:len_stream
            rubik(x,y,z) = stream_string ((x+y+z));
        end
    end
end
fprintf('%f',rubik);
eord=input('Encrypt or Decrypt ?...(type 1 or 2)');
switch eord 
    case 1
        %time to encrypt..learn how to use functions
        rubik=Encrypt(rubik);
    case 2
        rubik=Decrypt(rubik);
        % time to decrypt

end








function [rubik] = XRot(xturns , rubik)
%XRot rotates every odd plane for Xturns
%   Detailed explanation goes here
for xa=1:2:len_stream
    rubik(xa,:,:)= rot90(rubik(xa,:,:) , xturns);
end
end

function [rubik] = YRot( yturns , rubik )
%
for ya=1:2:len_stream
    rubik(:,ya,:)= rot90(rubik(:,ya,:) , yturns);
end
end

function [ rubik ] = ZRot( zturns , rubik )

for za=1:2:len_stream
    rubik(:,:,za)= rot90(rubik(:,:,za) , zturns);
end
end




function [rubik] = Encrypt(rubik)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
ekey= input ('Encryption:   enter 7 digit passkey [x x x x x x x]:  ');
shfl_seq = ekey(1);
xturns= ekey(2);
%xstyle= ekey(3);%style variables have to do with mat file PatternCommand
yturns= ekey(4);
%ystyle= ekey(5);
zturns= ekey(6);
%zstyle= ekey(7);
switch shfl_seq
    case 0
        %style is XYZ
        rubik = XRot(xturns , rubik);
        rubik = YRot(yturns , rubik);
        rubik = ZRot(zturns , rubik);
        %call xrot for Xturns also parse to it Xtsyle
        %then do for Y
        %then do for Z
    case 1
        %style is XZY
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns , rubik);
        rubik = YRot(yturns , rubik);
        
    case 2
        %style is YXZ
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns , rubik);
        
       
    case 3
        %style is YZX
        rubik = YRot(yturns , rubik);
        rubik = ZRot(zturns , rubik);
        rubik = XRot(xturns , rubik);
              
    case 4
        %style is ZXY
        rubik = ZRot(zturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = YRot(yturns , rubik);
    case 5
        %style is ZYX
        rubik = ZRot(zturns , rubik);
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns , rubik);
                
    case 6
        %style is -XYZ
        rubik = XRot(xturns*-1 , rubik);
        rubik = YRot(yturns , rubik);
        rubik = ZRot(zturns , rubik);
    case 7
        %style is -YXZ
        rubik = YRot(yturns*-1 , rubik);
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns , rubik);
    case 8
        %style is -ZXY
        rubik = ZRot(zturns*-1 , rubik);
        rubik = XRot(xturns , rubik);
        rubik = YRot(yturns , rubik);
    case 9
        %style is -X-Y-Z
        rubik = XRot(xturns*-1 , rubik);
        rubik = YRot(yturns*-1 , rubik);
        rubik = ZRot(zturns*-1 , rubik);
end
end
% For now lets keep the funcionality to only even step unidirectional
% rotation

% within the cases


function [rubik] = Decrypt(rubik)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
ekey= input ('Decryption:   enter 7 digit passkey :  ');
shfl_seq = ekey(1);
xturns= ekey(2)*-1;
%xstyle= ekey(3);%style variables have to do with mat file PatternCommand
yturns= ekey(4)*-1;
%ystyle= ekey(5);
zturns= ekey(6)*-1;
%zstyle= ekey(7);
switch shfl_seq
    case 0
        %style is XYZ
        rubik = ZRot(zturns , rubik);
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns , rubik);
        %call xrot for Xturns also parse to it Xtsyle
        %then do for Y
        %then do for Z
    case 1
        %style is XZY
        rubik = YRot(yturns , rubik);
        rubik = ZRot(zturns , rubik);
        rubik = XRot(xturns , rubik);
        
    case 2
        %style is YXZ
        rubik = ZRot(zturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = YRot(yturns , rubik);
       
        
       
    case 3
        %style is YZX
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns , rubik);
        rubik = YRot(yturns , rubik);   
        
    case 4
        %style is ZXY
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns , rubik);
        
    case 5
        %style is ZYX
        rubik = XRot(xturns , rubik);        
        rubik = YRot(yturns , rubik);
        rubik = ZRot(zturns , rubik);
                
    case 6
        %style is -XYZ
        rubik = ZRot(zturns , rubik);
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns*-1 , rubik);
        
    case 7
        %style is -YXZ
        rubik = ZRot(zturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = YRot(yturns*-1 , rubik);
        
    case 8
        %style is -ZXY
        rubik = YRot(yturns , rubik);
        rubik = XRot(xturns , rubik);
        rubik = ZRot(zturns*-1 , rubik);
        
    case 9
        %style is -X-Y-Z
        rubik = ZRot(zturns*-1 , rubik);
        rubik = YRot(yturns*-1 , rubik);
        rubik = XRot(xturns*-1 , rubik);

end
end
% For now lets keep the funcionality to only even step unidirectional
% rotation

% within the cases





