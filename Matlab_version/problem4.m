clc; 
clear; 
close all;

% Program No. 4
% For parameters, take NIM 13123031 (custom)
E = 23031;           % kg/mm^2
I = 1500;            % mm^4
M = 3031;            % mm·kg
L = 200;             % mm
h = 20;              % mm
N = L/h;             % Number of steps
x = 0:h:L;

% The direction of moment is negative, so the equation is negative.
alpha = -M / (E * I); 

% Arrays
y_rk2 = zeros(1, N+1); z_rk2 = zeros(1, N+1);
y_rk4 = zeros(1, N+1); z_rk4 = zeros(1, N+1);

% Initial conditions
y_rk2(1) = 0; z_rk2(1) = 0;
y_rk4(1) = 0; z_rk4(1) = 0;

% RK2 : Modified Euler
for n = 1:N
    k1y = h * z_rk2(n);
    k1z = h * alpha * (1 + z_rk2(n)^2)^(3/2);

    y_temp = y_rk2(n) + k1y;
    z_temp = z_rk2(n) + k1z;

    k2y = h * z_temp;
    k2z = h * alpha * (1 + z_temp^2)^(3/2);

    y_rk2(n+1) = y_rk2(n) + 0.5 * (k1y + k2y);
    z_rk2(n+1) = z_rk2(n) + 0.5 * (k1z + k2z);
end

% RK4
for n = 1:N
    k1y = h * z_rk4(n);
    k1z = h * alpha * (1 + z_rk4(n)^2)^(3/2);

    k2y = h * (z_rk4(n) + 0.5 * k1z);
    k2z = h * alpha * (1 + (z_rk4(n) + 0.5 * k1z)^2)^(3/2);

    k3y = h * (z_rk4(n) + 0.5 * k2z);
    k3z = h * alpha * (1 + (z_rk4(n) + 0.5 * k2z)^2)^(3/2);

    k4y = h * (z_rk4(n) + k3z);
    k4z = h * alpha * (1 + (z_rk4(n) + k3z)^2)^(3/2);

    y_rk4(n+1) = y_rk4(n) + (k1y + 2*k2y + 2*k3y + k4y)/6;
    z_rk4(n+1) = z_rk4(n) + (k1z + 2*k2z + 2*k3z + k4z)/6;
end

% The graph
figure;
plot(x, y_rk2, 'ro--', 'LineWidth', 1.8); hold on;
plot(x, y_rk4, 'b*-', 'LineWidth', 1.8);
xlabel('x (mm)'); ylabel('Deflection y(x) [mm]');
title('Beam Deflection using RK2 vs RK4');
legend('2nd-Order RK (Modified Euler)', '4th-Order RK', 'Location', 'SouthEast');
grid on;