function [ output_args ] = PaternCommand( input_args )
%  this function simply takes 3 inputs :
% plane... x,y,z
% no of turns
% style of encryption

%% fix-spin-antispin means keep one layer there , spin the next one , and
%% the next one to next to be spinned in the opposite direction

switch
    case 0 :
        %style is fix-spin
    case 1
        %style is fix-fix-spin
    case 2
        %style is fix-fix-spin-spin
    case 3
        %style is fix-fix-antispin
    case 4
        %style is fix-fix-antispin-antispin
    case 5
        %style is fix-spin-fix-antispin
    case 6
        %style is fix-antispin-fix-spin
    case 7
        %style is fix-spin-antispin-fix
    case 8
        %style is fix-spin-antispin-spin-fix
    case 9
        %style is fix-antispin-spin-antispin-fix






end

