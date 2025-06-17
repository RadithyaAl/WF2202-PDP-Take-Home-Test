% Parameter
terms = 100;         % Jumlah suku dalam deret Fourier
x = linspace(0, 1, 100);  % Posisi dari 0 sampai 1
t_vals = linspace(0, 3, 10);  % Waktu dari 0 sampai 3 dalam 10 langkah

% Preallocasi hasil
y = zeros(length(t_vals), length(x));

% Hitung suhu untuk tiap waktu dan posisi
for ti = 1:length(t_vals)
    t = t_vals(ti);
    for xi = 1:length(x)
        sum_val = 0;
        for n = 1:2:(2*terms - 1)  % hanya n ganjil
            term = (-800 / (n * pi)) * sin(n * pi * x(xi)) * exp(-0.1 * (n * pi)^2 * t);
            sum_val = sum_val + term;
        end
        y(ti, xi) = 300 + sum_val;
    end
end

% Plot
figure;
hold on;
colors = jet(length(t_vals));
for ti = 1:length(t_vals)
    plot(x, y(ti, :), 'DisplayName', sprintf('t = %.2f h', t_vals(ti)), 'Color', colors(ti, :));
end
xlabel('Position');
ylabel('Temperature');
title('Temperature Distribution Over Time (Analytical Solution)');
legend('Location', 'eastoutside');
grid on;
