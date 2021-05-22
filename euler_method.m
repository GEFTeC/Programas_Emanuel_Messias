clc
clear
f = @(x,y) x+y;
x0 = 0;
y0 = 1;
h = 0.1;
xn = 10;
n=(xn-x0)/h;
x(1)=x0; y(1)=y0;
for i=1:n
  x(i+1)=x(i)+h;
  #Explicit Method
  y(i+1)=y(i)+h*f(x(i),y(i));
  #Implicit Method
  ya(i+1)=y(i)+h*f(x(i+1),y(i+1));
end
a = 0:0.1:xn;
plot(a,2*exp(a)-a-1,'o');
hold on;
plot(x,y,'b+'); 
hold on;
plot(x,ya, 'ro');
legend ({"Exact Solution", "Explicit Method", "Implicit Method"});
print -dpng figure.png figure



