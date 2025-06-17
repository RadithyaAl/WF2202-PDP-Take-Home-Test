clc; 
clear;

% Program No. 2
L = 1; alpha = 0.1; Ti = 100; Ts = 300;
dx = 0.05; dt_values = [0.005, 0.01, 0.05];
x = 0:dx:L; nx = length(x);
t_final = 0.5;

for k = 1:length(dt_values)
    dt = dt_values(k);
    r = alpha * dt / dx^2;
    nt = round(t_final / dt);
    T = Ti * ones(1, nx);
    T(1) = Ts; T(end) = Ts;

    for n = 1:nt
        T_old = T;
        for i = 2:nx-1
            T(i) = T_old(i) + r * (T_old(i+1) - 2*T_old(i) + T_old(i-1));
        end
    end

    figure(k);
    plot(x, T, 'r-o'); grid on;
    title(["FTCS at \Delta t = ", num2str(dt), " hr"]);
    xlabel('x (ft)'); ylabel('Temperature (^\circF)');
end