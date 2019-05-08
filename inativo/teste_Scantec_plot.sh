#!/bin/bash

echo "Digite o periodo inicial: yyyymmddhh"
read datainicial

#variavel finaliza a contagem infinita gerada
echo "Digite o periodo final: yyyymmddhh"
read final

echo "     "

#incremento
incr=`echo ${datainicial} |cut -c9-10`

gnuplot=/stornext/home/carlos.bastarz/tools/gnuplot-5.0.0/bin/gnuplot 


#modelo
#gnuplot-c plot_scamtec_results.gpl 2015050106 2015050106

while : ;do

    datafi=$($inctime ${datainicial} +${incr}h %y4%m2%d2%h2)
    let incr=$incr+06
    echo ${datafi}

   ${gnuplot} -c plot_scamtec_results.gpl ${datafi} ${datafi}
    
    echo "plot_scamtec_results.gpl ${datafi} ${datafi} "
    mv plot_SCANTEC_results.eps plot_SCANTEC_results_${datafi}.eps    
  
    #Assim que alcancar a data final desejada, ele realiza um break nesse looping infinito
       if [ ${datafi} -eq ${final} ]
    then
       break
    fi
done
