set terminal pdfcairo font "Gill Sans, 9" linewidth 4 rounded fontscale 1.0 #size 6,3

set loadpath '~/.gpconfig/'

load 'pal/set1.pal'
load 'cfg/plot.cfg'
load 'cfg/grid.cfg'

set title "Density along fibril \n in the n-layer model"
set xlabel "x [nm]"
set ylabel "Counts"

set key top right
#set rmargin 10
#set key at screen 1, graph 1
set key samplen 1 spacing 1.0 font ",7"
set key off

#set xrange [0:1000]
set yrange [0:7]

x=0
outfile = sprintf('density%04.0f.pdf', x)
set output outfile
infile = sprintf('v2_N=1054_nPos=86_nNeg=82_layers=5_densities/density%.0f',x)
plot infile u 1:2 w l ls 1 lw 0.5 title 'Random'

#do for [t=x:x] {
#	outfile = sprintf('./Adensity%03.0f.pdf', t)
#	set output outfile
#	infile = sprintf('./test_N=1054_nPos=43_nNeg=41_layers=5.density%.0f',t)
#	plot infile u 1:2 w l ls (t+1) lw 0.5 title 'Random '.(t+1)
#}

