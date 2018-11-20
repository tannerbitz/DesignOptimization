% Armijo line search
function [a, w] = lineSearch(f, df, g, dg, x, s, mu_old, w_old)
    t = 0.1; % scale factor on current gradient: [0.01, 0.3]
    b = 0.8; % scale factor on backtracking: [0.1, 0.8]
    a = 1; % maximum step length
    
    D = s;                  % direction for x
    
    % Calculate weights in the merit function using eaution (7.77)
%     w = ***;
    % terminate if line search takes too long
    count = 0;
    while count<100
        % Calculate phi(alpha) using merit function in (7.76)
%         phi_a = ***;
        
        % Caluclate psi(alpha) in the line search using phi(alpha)
%         phi0 = ***;                   % phi(0)
%         dphi0 = ***;                  % phi'(0)
%         psi_a = ***;                  % psi(alpha) = phi(0)+t*alpha*phi'(0)
        
        % stop if condition satisfied
%         stop = ***
        if stop;
            break;
        else
            % backtracking
            a = a*b;
            count = count + 1;
        end
    end
end