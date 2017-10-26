#!/bin/bash
#if (...) then ... fi
<<'END'
a=$1
if (( $a > 0 ))
then
  echo "Izdruka no galvenā zara (ja gadijumā), tad, kad $a>0"
fi
  echo "Šī izdruka tiks veikta jebkurā gadijumā"
END

<<'END'
a=$1
if (( $a > 0 ))
then
  echo "Izdruka no galvenā zara (ja gadijumā), tad, kad $a>0"
else
  echo "Izdruka no galvenā zara (nē gadijumā), tad, kad $a nav >0"
fi
  echo "Šī izdruka tiks veikta jebkurā gadijumā"
END

a=$1
if (( $a > 0 ))
then
  echo "Izdruka no galvenā zara (ja gadijumā), tad, kad $a>0"
elif(( $a == 0 )); then
  echo "Atlikušais zars (ja gadijumā),tad ,kad $a ir = 0"
else
  echo "Galvena zara (visi atliku·ši gadijumi)"
  echo "Viennozīmīgais nē visiem iepriekšējiem gadījumiem"
fi
echo "Šī izdruka tiks veikta jebkurā gadijumā"

