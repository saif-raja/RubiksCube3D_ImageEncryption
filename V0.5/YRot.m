function [rubik] = YRot( yturns , rubik , len_stream )
%YRot rotates every odd plane for Y turns

tempslice = zeros(len_stream);
for ya=1:1:(len_stream)
    for i=1:1:(len_stream)
        for j=1:1:(len_stream)
            tempslice(i,j) = rubik(i,ya,j);
        end
    end
    tempslice = rot90(tempslice , yturns);
    for i=1:1:(len_stream)
        for j=1:1:(len_stream)
            rubik(i,ya,j) = tempslice(i,j);
        end
    end
    
end
end

