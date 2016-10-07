close all;

figure;
fplot(@(x) 0.5*x^2, [1, 10], '-r', 'Linewidth', 2);
hold on;
fplot(@(x) 3*x^2 + 1/2*x, [1, 10], '-b', 'Linewidth', 2);
fplot(@(x) 2*x^2 + 50, [1, 10], '-g', 'Linewidth', 2);
hold off;

ylabel('Runtime');
xlabel('Input elements');
%title('Squared runtime');
legend('1/2 x^2', '3 x^2 + 1/2 x', '2 x^2 + 50', 'Location', 'northwest');