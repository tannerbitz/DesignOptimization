function f = mae598_desopt_hw3_p1(a)
    % a(1) = A12
    % a(2) = A21
    
    %Calc psat for water, 1,4 dioxane
    a1_wat = 8.07131;
    a2_wat = 1730.63;
    a3_wat = 233.426;
    a1_dxn = 7.43155;
    a2_dxn = 1554.679;
    a3_dxn = 240.337;
    T = 20;
    psat_wat = 10^(a1_wat - a2_wat/(T+a3_wat));
    psat_dxn = 10^(a1_dxn - a2_dxn/(T+a3_dxn));
    
    % Data
    x1 = 0:0.1:1;
    x2 = ones(size(x1))-x1;
    y = [28.1, 34.4, 36.7, 36.9, 36.8, 36.7, 36.5, 35.4, 32.9, 27.7, 17.5];
    f = zeros(length(x1),1);
    
    %Calculate f
    for i = 1:length(x1)
        e1inner = a(1)*(a(2)*x2(i)/(a(1)*x1(i) + a(2)*x2(i)))^2;
        e2inner = a(2)*(a(1)*x1(i)/(a(1)*x1(i) + a(2)*x2(i)))^2;
        f(i) = x1(i)*exp(e1inner)*psat_wat + x2(i)*exp(e2inner)*psat_dxn - y(i);
    end
end