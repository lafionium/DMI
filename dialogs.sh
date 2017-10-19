#!/bin/bash
echo "lūdzu ievadi pirmo skaitli"
read a
echo "lūdzu ievadi otro skaitli"
read b
c=`expr $a + $b`
echo "$a + $b = "$c
