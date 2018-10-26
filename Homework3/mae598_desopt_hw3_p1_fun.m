function f = mae598_desopt_hw3_p1_fun(x)
    A12 = 1.9584;
    A21 = 1.6892;

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


    e1inner = A12*(A21*x(2)/(A12*x(1) + A21*x(2)))^2;
    e2inner = A21*(A12*x(1)/(A12*x(1) + A21*x(2)))^2;
    f = x(1)*exp(e1inner)*psat_wat + x(2)*exp(e2inner)*psat_dxn;
end