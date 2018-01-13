#!/bin/bash
echo "pirmais skaitlis - a"
read a
echo "otrais skaitli - b"
read b
echo "trešais skaitlis - c"
read c

: <<'END'
#divi skaitli
if [ $a -eq $b ]
then
echo "a ($a) =  b ($b)"
fi

if [ $a -gt $b ]
then
echo " a ($a) > b ($b)"
fi

if [ $a -lt $b ]
then
echo " a ($a) < b ($b)"
fi
END

: <<'END'
if [ $a -gt $b == $c ]
then
echo " a ($a) > b ($b) = c ($c)"
fi

if [ $a == $b -gt $c ]
then
echo " a ($a) = b ($b) > c ($c)"
fi

if [ $a -lt $b == $c ]
then
echo " a ($a) < b ($b) = c ($c)"
fi

if [ $a == $b -lt $c ]
then
echo " a ($a) = b ($b) < c ($c)"
fi
END


: <<'END'
if (( $a > $b && $a > $c ))
then
echo " a ($a) - lielākais skaitlis"
elif (( $b > $a && $b >  $c ))
then
echo " b ($b) - lielākais skaitlis"
elif (( $c > $b && $c > $a ))
then
echo " c ($c) - lilākais skaitlis"
fi
END

: <<'END'
if (( $a > $b && $a > $c ))
then
 if (( $b > $c ))
 then
  echo " ($a) ($b) ($c)"
# elif (( $b < $c ))
# then
 else
  echo " ($a) ($c) ($b)"
 fi
fi
END

if (( $b > $a && $b > $c ))
 then
  if (( $a > $c))
   then
    echo " ($b) ($a) ($c)"
  elif (( $a < $c ))
   then
    echo " ($b) ($c) ($a)"
  fi
fi


if (( $c > $b && $c > $a ))
 then
  if (( $b > $a))
   then
    echo " ($c) ($b) ($a)"
  elif (( $b < $a ))
   then
    echo " ($c) ($a) ($b)"
  fi
fi

