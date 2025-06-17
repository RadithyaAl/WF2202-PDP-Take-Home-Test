clc;
clear;

% Program for no. 1 
n = input('Enter the number of equations (n): ');

fprintf('Enter the coefficient matrix A (%dx%d):\n', n, n);
A = zeros(n);
for i = 1:n
    for j = 1:n
        A(i,j) = input(sprintf('A(%d,%d): ', i, j));
    end
end

fprintf('Enter the constant vector b (%dx1):\n', n);
b = zeros(n,1);
for i = 1:n
    b(i) = input(sprintf('b(%d): ', i));
    % OR: input('b(%d): ') for dynamic prompt
end

method = input('Choose method: A (Gauss Elimination), B (Gauss Seidel): ', 's');

if upper(method) == 'A'
    % ----------- GAUSS ELIMINATION METHOD -----------
    Aug = [A b];  % Augmented matrix
    
    % Forward Elimination
    for i = 1:n-1
        for j = i+1:n
            if Aug(i,i) == 0
                error('Division by zero detected!');
            end
            factor = Aug(j,i)/Aug(i,i);
            Aug(j,:) = Aug(j,:) - factor * Aug(i,:);
        end
    end

    % back substitution
    x = zeros(n,1);
    x(n) = Aug(n,end)/Aug(n,n);
    for i = n-1:-1:1
        x(i) = (Aug(i,end) - Aug(i,i+1:n)*x(i+1:n)) / Aug(i,i);
    end

    fprintf('\nSolution using Gauss Elimination:\n');
    for i = 1:n
        fprintf('X%d = %.4f\n', i, x(i));
    end

elseif upper(method) == 'B'
    % Gauss-Seidel Method
    x = zeros(n,1); % Initial guess
    tol = 1e-4;     % Tolerance
    max_iter = 100; % Max iterations

    fprintf('\nIterative solution using Gauss-Seidel:\n');
    for iter = 1:max_iter
        x_old = x;
        for i = 1:n
            sum1 = A(i,1:i-1)*x(1:i-1);
            sum2 = A(i,i+1:n)*x_old(i+1:n);
            if A(i,i) == 0
                error('Zero diagonal element detected!');
            end
            x(i) = (b(i) - sum1 - sum2)/A(i,i);
        end
        
        fprintf('Iteration %d: ', iter);
        fprintf('X = [');
        fprintf('%.4f ', x);
        fprintf(']\n');
        
        if norm(x - x_old, inf) < tol
            break;
        end
    end

    fprintf('\nFinal solution after %d iterations:\n', iter);
    for i = 1:n
        display('X%d = %.4f\n', i, x(i));
    end

else
    fprintf('Invalid method choice. Please enter A or B.\n');
end
