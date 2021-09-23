function [rubik] = XYZDec( axis , turns , rubik , len_stream , spinpos)
%decides which axis mainpulaiton to go with 
switch axis
    case 1
        xa = spinpos;
        rubik = XRot1(turns , rubik , len_stream , xa);
    case 2
        ya = spinpos;
        rubik = YRot1(turns , rubik , len_stream , ya);
    case 3
        za = spinpos;
        rubik = ZRot1(turns , rubik , len_stream , za);
end

