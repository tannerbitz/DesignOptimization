syms x1 x2 A12 A21 p1 p2

e1inner = A12*(A21*x2/(A12*x1+A21*x2))^2;
e2inner = A21*(A12*x1/(A12*x1+A21*x2))^2;

f = x1*exp(e1inner)*p1 + x2*exp(e2inner)*p2;

g = gradient(f, [A12, A21])

%% lsqnonlin
a0 = [1, 1];
options = optimoptions(@lsqnonlin, 'Algorithm', 'trust-region-reflective');
a = lsqnonlin(@mae598_desopt_hw3_p1, a0, [], [], options)


%% Check lsqnonlin solution with plot
x1 = 0:0.1:1;
x2 = ones(size(x1))-x1;
y = [28.1, 34.4, 36.7, 36.9, 36.8, 36.7, 36.5, 35.4, 32.9, 27.7, 17.5];

j = 1;
for i = 0:0.005:1
    x_blah(j) = i;
    x = [i, 1-i];
    f(j) = mae598_desopt_hw3_p1_fun(x);
    j = j + 1;
end

close all
figure(1)
plot(x1, y, 'ro');
hold on
plot(x_blah, f);
hold off
legend('Data', 'Fitted Curve')
title('Fitting with lsqnonlin')
xlabel('x1')
ylabel('y')


%% Problem 2
load homework3data.mat
neuralnet = fitnet();
neuralnet.divideParam.trainRatio = 0.7;
neuralnet.divideParam.valRatio = 0.15;
neuralnet.divideParam.testRatio = 0.15;

train(neuralnet, X', y')
