close all;

figure;
fplot(@(x) 22*x, [1, 10], '-b', 'Linewidth', 2);
hold on;
fplot(@(x) 5*x^2 + 10, [1, 10], '-g', 'Linewidth', 2);
fplot(@(x) 0.75*x^3, [1, 10], '-r', 'Linewidth', 2);
line([3.88, 3.88],[0, 800]);
line([5.42, 5.42],[0, 800]);
%line([6.95, 6.95],[0, 800]);
hold off;

ylabel('Runtime');
xlabel('Input elements');
%title('Squared runtime');
legend('g(n) = n', 'f_1(n) = 2 n^2 + 10', 'f_2(n) = 3/4 n^3', 'Location', 'northwest');