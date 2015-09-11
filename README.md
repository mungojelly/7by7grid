#7by7grid
A very simple space where programs can play with color.

7by7grid is mostly intended for very early beginning programmers. The
first thing you learn in every introduction to every language is
reading input and printing some simple text-- but it's rarely clear
how to go from there to making anything pretty or interesting happen.
So this is an example of a very simple interface that anyone can
engage with right after printing their first hello world.

To print something that will work with the other programs in 7by7grid,
just print out 49 colors in the normal 6-digit long hex format (like
\#FF0000 for red) separated by any amount of whitespace (like spaces
and newlines).

To minimize confusion, all of the programs here should be
deterministic (they don't have any "random" statements) and stateless
(they don't write anything to disk), in other words their output
should differ only if they're given a different input.

Each program in 7by7grid should fit onto a single slide or screenshot,
so hopefully there are examples here that are simple enough for you to
follow. Feel free to submit new programs, even if they're just small
modifications to these existing programs.

```
[mungojelly@localhost py]$ python limegray.py 
#a0a0a0 #ab958a #b8a172 #c7c758 #a4d83d #63eb1f #00ff00
#909090 #9f8579 #af9560 #c1c146 #9cd42a #59e215 #00ee00
#808080 #927668 #a38851 #b3b33c #8ec227 #52d013 #00dd00
#707070 #81685c #917948 #a0a035 #81b023 #4bbe11 #00cc00
#606060 #705a50 #7f6a3f #8e8e2f #739d1f #44ac10 #00bb00
#505050 #5e4c43 #6d5b36 #7c7c29 #668b1c #3d9a0e #00aa00
#404040 #4d3e37 #5b4c2d #696923 #587918 #36880c #009900
[mungojelly@localhost py]$ python limegray.py | python darken.py 
#505050  #5a4941  #635332  #6b6b24  #547317  #307a0b  #007f00 
#484848  #52423a  #5a4b2d  #626221  #4e6a15  #2c710a  #007700 
#404040  #493b34  #514428  #59591e  #476113  #296809  #006e00 
#383838  #40342e  #483c24  #50501a  #405811  #255f08  #006600 
#303030  #382d28  #3f351f  #474717  #394e0f  #225608  #005d00 
#282828  #2f2621  #362d1b  #3e3e14  #33450e  #1e4d07  #005500 
#202020  #261f1b  #2d2616  #343411  #2c3c0c  #1b4406  #004c00 
[mungojelly@localhost py]$ python limegray.py | python darken.py | python htmldisplay.py > example.html
```
