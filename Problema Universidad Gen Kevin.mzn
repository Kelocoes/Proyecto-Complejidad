int: n;
int: m;
array [1..m,1..2] of int: ciudades;
array [1..m] of var int: distancias;
var int: posX;
var int: posY;

constraint posX >= 0 /\ posX <= n;
constraint posY >= 0 /\ posY <= n;
constraint forall(i in 1..m) (not (posX == ciudades[i,1] /\ posY == ciudades[i,2]));
constraint forall(i in 1..m) (distancias[i] = abs(posX - ciudades[i,1]) + abs(posY - ciudades[i,2]));

solve minimize max(distancias);

