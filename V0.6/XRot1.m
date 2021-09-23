function [rubik] = XRot1( xturns , rubik , len_stream , xa )
%XRot rotates every odd plane for Xturns


tempslice = zeros(len_stream);

for i=1:1:(len_stream)
    for j=1:1:(len_stream)
        tempslice(i,j) = rubik(xa,i,j);
    end
end
tempslice = rot90(tempslice , xturns);
for i=1:1:(len_stream)
    for j=1:1:(len_stream)
        rubik(xa,i,j) = tempslice(i,j);
    end
end
end

