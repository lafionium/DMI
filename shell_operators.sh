#!/bin/bash

echo "________________________"
#1. piemērs (mērķis 2+2=4)
# - gala rezultāts simbolu rinda "2+2" nevis skaitlis 4
val=2+2
echo "Bez apostrofiem "$val

#2. piemērs (mērķis 2+2=4)
:<<'END'
val1=`expr 2+2`
echo "Neparasti apostrofi bez atstarpēm "$val1
val2='expr 2+2'
echo "Partasti apostrofi bez atstarpēm "$val2
val3=`expr 2 + 2`
echo "Neparasti apostrofi ar atstarpēm DARBOJĀS "$val3
val4='expr 2 + 2'
echo "Parasti apostrofi ar atstarpēm "$val4


#2.1. piemērs (mērķis 5-2=3)
val1=`expr 5 - 2`
echo "nuzno eto echo objazatelno.... "$val1
END

# 3. piemērs (+ ,- ,* ,/)
#: << 'END'
val31=`expr 2 + 3`
echo "2 + 3 = "$val31
val32=`expr 2 - 3`
echo "2 - 3 = "$val32
val33=`expr 2 \* 3`
echo "2 * 3 = "$val33
val34=`expr 2 / 3`
echo "2  / 3 = "$val34
val35=`expr 5 % 3`
echo "5 % 3 = "$val31
#END


