clc;
clear;

% Program No. 3
N = 5; % 5x5 grid (including boundaries)
T = zeros(N); % Initial temperature grid

% Boundary Conditions, let NIM 13123031
T_top = 131;
T_bottom = 3;
T_left = 1;
T_right = 23;

% Apply boundary conditions
T(1,:) = T_top;         % Top row
T(N,:) = T_bottom;      % Bottom row
T(:,1) = T_left;        % Left column
T(:,N) = T_right;       % Right column

% Convergence criteria
eps = 1;  % convergence error in percent
error = 100; % initial error
iteration = 0;

% Gauss-Seidel iteration
while error > eps
    T_old = T;
    for i = 2:N-1
        for j = 2:N-1
            T(i,j) = 0.25 * (T(i+1,j) + T(i-1,j) + T(i,j+1) + T(i,j-1));
        end
    end
    iteration = iteration + 1;
    error = max(max(abs((T - T_old) ./ T) * 100));
end

% Final temperature distribution
fprintf('Converged after %d iterations.\n', iteration);
disp('Temperature distribution at interior points:');
disp(T(2:N-1, 2:N-1));

% Show the graph
[X, Y] = meshgrid(1:N, 1:N);
figure;
surf(X, Y, T, 'EdgeColor', 'none');
colorbar;
title('Steady-State Temperature Distribution');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Temperature (°C)');