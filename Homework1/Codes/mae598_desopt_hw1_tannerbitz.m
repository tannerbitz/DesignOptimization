% Tanner Bitz
% MAE 598: Design Optimization
% Fall 2018
% HW 1
%% problem 1
clear all; clc;
fun = @(x) 24.55*x(1) + 26.75*x(2) + 39.00*x(3) + 40.50*x(4);
x0 = [1,1,1,1];
A = [-2.3, -5.6, -11.1, -1.3;
       -1,    0,     0,    0;
        0,   -1,     0,    0;
        0,    0,    -1,    0;
        0,    0,     0,   -1];
 
b = [-5, 0, 0, 0 ,0]';
Aeq = [1, 1, 1, 1];
beq = 1;
lb = [];
ub = [];
nonlcon = @p1_nonlincon;
x = fmincon(fun, x0, A, b, Aeq, beq, lb, ub, nonlcon)

%% problem 2
clear all; clc;
% I am minimizing the surface area of a cyclindrical soda can.
%   x(1) - radius of soda can
%   x(2) - height (or length) of soda can
f = @(x) 2*pi*x(1)*x(2) + 2*pi*x(1)^2;  %minimize surface area
x0 = [1,1];                             %initial guess
A = -eye(2);                                
b = zeros(1,2);
Aeq = [];
beq = [];
lb = [];
ub = [];
nonlcon = @p2_nonlincon;
x = fmincon(f, x0, A, b, Aeq, beq, lb, ub, nonlcon)
cm2inches = 0.393701;
x_inches = x*cm2inches

%% problem 3
clear all; clc;
% integer programming solution 
f = [5, 6, 7]';     % minimizing the total cost given protein/vitamin constraints
intcon = 1:3;       % all variables are integers
A = [-5,  0, -3;
      0, -6, -2;
     -1,  0,  0;
      0, -1,  0;
      0,  0, -1];
b = [-10, -20, 0, 0, 0]';

x = intlinprog(f, intcon, A, b)
integer_optimal_cost = 5*x(1) + 6*x(2) + 7*x(3)

% linear progamming (not integer variable constrained) solution
% A = x(1)
% B = x(2)
% C = x(3)
fun = @(x) 5*x(1) + 6*x(2) + 7*x(3);
x0 = [0, 0, 0]';
y = fmincon(fun, x0, A, b) 
optimal_cost = fun(y)