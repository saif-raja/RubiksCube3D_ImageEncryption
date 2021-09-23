%ZRot rotates every odd plane for Zturns
function [ rubik ] = ZRot( zturns , rubik , len_stream )

tempslice = zeros(len_stream);
for za=1:1:(len_stream)
    for i=1:1:(len_stream)
        for j=1:1:(len_stream)
            tempslice(i,j) = rubik(i,j,za);
        end
    end
    tempslice = rot90(tempslice , zturns);
    for i=1:1:(len_stream)
        for j=1:1:(len_stream)
            rubik(i,j,za) = tempslice(i,j);
        end
    end
    
end
end