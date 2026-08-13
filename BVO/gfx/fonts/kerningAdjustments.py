file = open( "DOSVGA.fnt", "wt" )

# Add the symbol positions of the blank symbol slots here.
exclude = [ 32 ]

for x in range( 1, 255 ):
    for y in range(1, 255):
        if x not in exclude:
            if y not in exclude:
                file.write( "kerning first={0}  second={1}  amount=1\n".format( x, y ) )

file.close()