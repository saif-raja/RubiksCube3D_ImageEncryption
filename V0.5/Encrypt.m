function [rubik] = Encrypt(rubik , len_stream)
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
        rubik = XRot(xturns , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
        %call xrot for Xturns also parse to it Xtsyle
        %then do for Y
        %then do for Z
    case 1
        %style is XZY
        rubik = XRot(xturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
        
    case 2
        %style is YXZ
        rubik = YRot(yturns , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
        
       
    case 3
        %style is YZX
        rubik = YRot(yturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
              
    case 4
        %style is ZXY
        rubik = ZRot(zturns , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
    case 5
        %style is ZYX
        rubik = ZRot(zturns , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
                
    case 6
        %style is -XYZ
        rubik = XRot(xturns*-1 , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
    case 7
        %style is -YXZ
        rubik = YRot(yturns*-1 , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
        rubik = ZRot(zturns , rubik , len_stream);
    case 8
        %style is -ZXY
        rubik = ZRot(zturns*-1 , rubik , len_stream);
        rubik = XRot(xturns , rubik , len_stream);
        rubik = YRot(yturns , rubik , len_stream);
    case 9
        %style is -X-Y-Z
        rubik = XRot(xturns*-1 , rubik , len_stream);
        rubik = YRot(yturns*-1 , rubik , len_stream);
        rubik = ZRot(zturns*-1 , rubik , len_stream);
end
% For now lets keep the funcionality to only even step unidirectional
% rotation

% within the cases











