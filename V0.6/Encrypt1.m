function [rubik] = Encrypt1(rubik , len_stream)
%Summary

ekey= input ('Encryption:   enter 7 digit passkey [x x x x x x x]:  ');
shfl_seq = ekey(1);
xturns= ekey(2);
xstyle= ekey(3);%style variables have to do with mat file PatternCommand
yturns= ekey(4);
ystyle= ekey(5);
zturns= ekey(6);
zstyle= ekey(7);
switch shfl_seq
    case 0
        %style is XYZ
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        %call xrot for Xturns also parse to it Xtsyle
        %then do for Y
        %then do for Z
    case 1
        %style is XZY
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        
    case 2
        %style is YXZ
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        
       
    case 3
        %style is YZX
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
              
    case 4
        %style is ZXY
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
    case 5
        %style is ZYX
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
                
    case 6
        %style is -XYZ
        rubik = PaternCommand( 1 , (xturns *-1) , rubik , len_stream , xstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
    case 7
        %style is -YXZ
        rubik = PaternCommand( 2 , (yturns *-1) , rubik , len_stream , ystyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 3 , zturns , rubik , len_stream , zstyle);
    case 8
        %style is -ZXY
        rubik = PaternCommand( 3 , (zturns *-1) , rubik , len_stream , zstyle);
        rubik = PaternCommand( 1 , xturns , rubik , len_stream , xstyle);
        rubik = PaternCommand( 2 , yturns , rubik , len_stream , ystyle);
    case 9
        %style is -X-Y-Z
        rubik = PaternCommand( 1 , (xturns *-1) , rubik , len_stream , xstyle);
        rubik = PaternCommand( 2 , (yturns *-1) , rubik , len_stream , ystyle);
        rubik = PaternCommand( 3 , (zturns *-1) , rubik , len_stream , zstyle);
end


