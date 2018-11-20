function [s, mu0] = solveqp(x, W, df, g, dg)
    % Implement an Active-Set strategy to solve the QP problem given by
    % min     (1/2)*s'*W*s + c'*s
    % s.t.    A*s-b <= 0
    % 
    % where As-b is the linearized active contraint set
    
    % Strategy should be as follows:
    % 1-) Start with empty working-set
    % 2-) Solve the problem using the working-set
    % 3-) Check the constraints and Lagrange multipliers
    % 4-) If all constraints are staisfied and Lagrange multipliers are positive, terminate!
    % 5-) If some Lagrange multipliers are negative or zero, find the most negative one 
    %     and remove it from the active set
    % 6-) If some constraints are violated, add the most violated one to the working set
    % 7-) Go to step 2
    
    
    % Compute c in the QP problem formulation
%     c = ***;     
    
    % Compute A in the QP problem formulation using all constraints
%     A0 = ***;           
    
    % Compute b in the QP problem formulation using all constraints
%     b0 = ***;           
    
    % Initialize variables for active-set strategy
    stop = 0;           % Start with stop = 0
    % Start with empty working-set
    A = [];         % A for empty working-set
    b = [];         % b for empty working-set
    % Indices of the constraints in the working-set
    active = [];    % Indices for empty-working set
    
    while ~stop  % Continue until stop = 1
        % Initialize all mu as zero and update the mu in the working set
%         mu0 = ***;
        
        % Extact A corresponding to the working-set from A0
%         A = ***;
        % Extract b corresponding to the working-set from b0
%         b = ***;
        
        % Solve the QP problem given A and b
        [s, mu] = solve_activeset(x, W, c, A, b);
        % Round mu to prevent numerical errors (Keep this)
        mu = round(mu*1e12)/1e12;
        
        % Update mu values for the working-set using the solved mu values
%         mu0(***) = ***;
        
        % Calculate the constraint values using the solved s values
%         gcheck = ***;
        
        % Round constraint values to prevent numerical errors (Keep this)
        gcheck = round(gcheck*1e12)/1e12;
        
        % Variable to check if all mu values make sense. 
        mucheck = 0;        % Initially set to 0
        
        % Indices of the constraints to be added to the working set
        Iadd = [];              % Initialize as empty vector
        % Indices of the constraints to be added to the working set
        Iremove = [];           % Initialize as empty vector 
        
        % Check mu values and set mucheck to 1 when they make sense
        if (numel(mu) == 0)
            % When there no mu values in the set
%             mucheck = ***;         % OK
        elseif min(mu) > 0
            % When all mu values in the set positive
%             mucheck = ***;         % OK
        else
            % When some of the mu are negative
            % Find the most negaitve mu and remove it from active set
%             Iremove = ***;  % Use Iremove to remove the constraint 
        end
        
        % Check if constraints are satisfied
        if max(gcheck) <= 0
            % If all constraints are satisfied
            if mucheck == 1
                % If all mu values are OK, terminate by setting stop = 1
%                 stop = ***;
            end
        else
            % If some constraints are violated 
            % Find the most violated one and add it to the working set
%             Iadd = ***; % Use Iadd to add the constraint
        end
        % Remove the index Iremove from the working-set
%         active = ***;
        % Add the index Iadd to the working-set
%         active = ***;
        
        % Make sure there are no duplications in the working-set (Keep this)
        active = unique(active);
    end 
end

function [s, mu] = solve_activeset(x, W, c, A, b)
    % Given an active set, solve QP
    
    % Create the linear set of equations given in equation (7.79)
%     M = ***;  
%     U = ***;
    sol = M\U;          % Solve for s and mu
    
%     s = ***;                % Extract s from the solution
%     mu = ***;    % Extract mu from the solution

end