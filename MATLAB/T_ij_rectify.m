clc
clear all

%disp('Define length of the area in x & y directions in meters for eg. x1 = 0:150:16000 & y1 = -10000:150:10000')
x1 = -10:.3:10;  % Define total x distance with spacing
y1 = -10:.3:10;    % Define total y distance with spacing
[x,y] = meshgrid(x1,y1);
%disp('Define the observation plane in terms of z for eg. 20 and  2.7 density in gm/cc')
z =5;   % the surface where data is computed

d = 11.11;    % geological density in gm/cc

A = 10^-3; % unit conversion from m to km
B = 1000; % unit conversion from mGal/km to E
G = 6.67384e-3;   % Define Gravitational constant
%c = G*d;  % multiplication of gravitational constant and density

%disp('Define the body parameters in meters for eg. xpos(1) = 4000; xpos(2) = 12000; ypos(1) = -2000; ypos(2) = 2000; zpos(1) = -1000; zpos(2) = -3000')
xpos(1) = 0; % % first corner of body along x-axis
xpos(2) = 2;   %second corner of body along x-axis
ypos(1) = 0;  % first corner of body along y-axis
ypos(2) = 2;  % second corner of body along y-axis
zpos(1) = 0;  % first corner of body along downward z-axis
zpos(2) = 2;  % second corner of body along downward z-axi

gxx = zeros(size(x))==0;
gxy = zeros(size(x))==0;
gyy = zeros(size(x))==0;
gzx = zeros(size(x))==0;
gyz = zeros(size(x))==0;
gzz = zeros(size(x))==0;

%function [gz1, gy1, gx1] = prismgrav(x, y, z, d, xpos, ypos, zpos)
for i=1:2
    for j=1:2
        for k=1:2
                r=((x-xpos(i)).^2+(y-ypos(j)).^2+(z-zpos(k)).^2).^0.5;
                if mod(i+j+k,2)==0
                    s=1;
                else
                    s=-1;
                end
                valuexx = G*d*s.*(atan((z-zpos(k)).*(y-ypos(j))./((x-xpos(i)).*r)));
                valuexy = G*d*s.*((-1).*log(r+(z-zpos(k))));
                valueyy = G*d*s.*(atan((z-zpos(k)).*(x-xpos(i))./((y-ypos(j)).*r)));
                valuezx = G*d*s.*((-1).*log(r+(y-ypos(j))));
                valueyz = G*d*s.*((-1).*log(r+(x-xpos(i))));
                %valuezz =-G*d*s*atan((x-xpos(i)).*(y-ypos(j))./((z-zpos(k)).*r));
                valuezz= G*d*s.*(atan((x-xpos(i)).*(y-ypos(j))./((z-zpos(k)).*r)));
                gxx = gxx + valuexx;
                gxy = gxy + valuexy;
                gyy = gyy + valueyy;
                gzx = gzx + valuezx;
                gyz = gyz + valueyz;
                gzz = gzz + valuezz;
        end
    end
end
 
u= valuezz+valuexx+valueyy;
             
% plotting the responses
figure;
%surf(x*A,y*A,gxx*B);   % 3D plot
surf(x,y,gxx*B);   % 3D plot
xlabel('x(m)');   % title for the horizontal axis
ylabel('y(m)');    % title for the vertical axis
zlabel('Txx(E) ');  % title for the anomaly axis
title(' Gravity Gradient(Txx)');   % title for the plot

% plotting new figure
figure;
surf(x,y,gxy*B);    %3D plot
xlabel('x(m)');   % title for the horizontal axis
ylabel('y(m)');    % title for the vertical axis
zlabel('Txy(E)');  % title for the anomaly axis
title(' Gravity Gradient(Txy)');   % title for the plot
% plotting new figure
figure;
surf(x,y,gyy*B);   % 3D plot
xlabel('x disance in m');   % title for the horizontal axis
ylabel('y distance in m');    % title for the vertical axis
zlabel('Tyy(E)');  % title for the anomaly axis
title(' Gravity Gradient(Tyy)');   % title for the plot
% plotting new figure
figure;
surf(x,y,gzx*B);     % 3D plot
xlabel('x(m)');   % title for the horizontal axis
ylabel('y(m)');    % title for the vertical axis
zlabel('Tzx(E)');  % title for the anomaly axis
title(' Gravity Gradient(Tzx)');  % title for the plot
% plotting new figure
figure;
surf(x,y,gyz*B);    % 3D plot
xlabel('x disance in m');   % title for the horizontal axis
ylabel('y distance in m');    % title for the vertical axis
zlabel('Tyz(E)');  % title for the anomaly axis
title(' Gravity Gradient(Tyz)');   % title for the plot
% plotting new figure
figure;
surf(x,y,gzz*B);   %3D plot
xlabel('x disance in m');   % title for the horizontal axis
ylabel('y distance in m');    % title for the vertical axis
zlabel('Tzz (E) ');  % title for the anomaly axis
title(' Gravity Gradient(Tzz)');  % title for the plot

