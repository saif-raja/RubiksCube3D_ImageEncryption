%Figurative main function , the starting point


display('Rubeka V 0.5');
global rubik ;
raw_string=input('Please enter the text');
stream_string=uint8(raw_string);
global len_stream;
len_stream = ceil(nthroot(length(stream_string) , 3));
rubik= ones(len_stream , len_stream , len_stream );
count=0;
stream_string = horzcat(stream_string , zeros( [1 , (len_stream.^3 - length(stream_string))]) );
for x=1:1:len_stream
    for y=1:1:len_stream
        for z=1:1:len_stream
            count=count+1;
            rubik(x,y,z) = stream_string (count);
        end
    end
end


eord=input('Encrypt or Decrypt ?...(type 1 or 2)');
switch eord 
    case 1
        rubik=Encrypt(rubik , len_stream);
    case 2
        rubik=Decrypt(rubik , len_stream);

end



countO=0;
for x=1:1:len_stream
    for y=1:1:len_stream
        for z=1:1:len_stream
            countO = countO + 1;
            Ostream_string ( countO ) = rubik(x,y,z);
        end
    end
end
out_string=char(Ostream_string);
out_string


