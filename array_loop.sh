#!/bin/bash
array=( "$@" )
N=$#
#echo array
#echo ${array[0]}- ievadam iebkuru skaitli un programma parada pirmo kas bija uzrakstits
#echo ${array[1]}
k=0
while (( $k < $N ))
do
  echo "Masīva $k.elements ir vienāds ar ${array[$k]}"
  k=`expr $k + 1`
done

<< 'END'
a=$1
b=$2
c=$3
END
