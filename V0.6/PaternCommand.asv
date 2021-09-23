function [ rubik ] = PaternCommand( axis , turns , rubik , len_stream , style)
%  this function simply takes 3 inputs :
% plane... x,y,z
% no of turns
% style of encryption

switch style
    case 0
        %style is fix-spin
        for i=1:1:len_stream
            if( mod(i,2) == 1)
                spinpos = i ;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
            end
        end
        
    case 1
        %style is fix-fix-spin
        for i=1:1:len_stream
            if( mod(i,3) == 0)
                spinpos = i -1 ;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
            end
        end
    case 2
        %style is fix-fix-spin-spin
        for i=1:1:len_stream
            if( mod(i,4) == 0)
                spinpos = i -2 ;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos +1);
            end
        end
    case 3
        %style is fix-fix-antispin
        for i=1:1:len_stream
            if( mod(i,3) == 0)
                spinpos = i -1 ;
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos);
            end
        end
    case 4
        %style is fix-fix-antispin-antispin
        for i=1:1:len_stream
            if( mod(i,4) == 0)
                spinpos = i -2 ;
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos +1);
            end
        end
    case 5
        %style is fix-spin-fix-antispin
        for i=1:1:len_stream
            if( mod(i,4) == 0)
                spinpos = i -3 ;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos +2);
            end
        end
    case 6
        %style is fix-antispin-fix-spin
        for i=1:1:len_stream
            if( mod(i,4) == 0)
                spinpos = i -3 ;
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos +2);
            end
        end
    case 7
        %style is fix-spin-antispin-fix
        for i=1:1:len_stream
            if( mod(i,4) == 0)
                spinpos = i -3;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos +2);
            end
        end
    case 8
        %style is fix-spin-antispin-spin-fix
        for i=1:1:len_stream
            if( mod(i,5) == 0)
                spinpos = i -4;
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos +1);
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos +2);
            end
        end
    case 9
        %style is fix-antispin-spin-antispin-fix
        for i=1:1:len_stream
            if( mod(i,5) == 0)
                spinpos = i -4;
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos);
                rubik = XYZDec( axis , turns , rubik , len_stream , spinpos +1);
                rubik = XYZDec( axis , (turns * -1) , rubik , len_stream , spinpos +2);
            end
        end

end

