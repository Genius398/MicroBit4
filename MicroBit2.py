from microbit import *
import radio
radio.config(group=7)
radio.on()
level=0
display.show(Image('00000:''00000:''00000:''00000:''00000'))
while True:
    message=radio.receive()
    if message=='low' and level!=1:
        level=level-1
        if level == 9:
            display.show(Image('99999:''99999:''99999:''99999:''99999'))
        elif level == 8:
            display.show(Image('88888:''88888:''88888:''88888:''88888'))
        elif level == 7:
            display.show(Image('77777:''77777:''77777:''77777:''77777'))
        elif level == 6:
            display.show(Image('66666:''66666:''66666:''66666:''66666'))
        elif level == 5:
            display.show(Image('55555:''55555:''55555:''55555:''55555'))
        elif level == 4:
            display.show(Image('44444:''44444:''44444:''44444:''44444'))
        elif level == 3:
            display.show(Image('33333:''33333:''33333:''33333:''33333'))
        elif level == 2:
            display.show(Image('22222:''22222:''22222:''22222:''22222'))
        elif level == 1:
            display.show(Image('11111:''11111:''11111:''11111:''11111'))

    if message == 'high' and level!=9:
        level=level+1
        if level == 9:
            display.show(Image('99999:''99999:''99999:''99999:''99999'))
        elif level == 8:
            display.show(Image('88888:''88888:''88888:''88888:''88888'))
        elif level == 7:
            display.show(Image('77777:''77777:''77777:''77777:''77777'))
        elif level == 6:
            display.show(Image('66666:''66666:''66666:''66666:''66666'))
        elif level == 5:
            display.show(Image('55555:''55555:''55555:''55555:''55555'))
        elif level == 4:
            display.show(Image('44444:''44444:''44444:''44444:''44444'))
        elif level == 3:
            display.show(Image('33333:''33333:''33333:''33333:''33333'))
        elif level == 2:
            display.show(Image('22222:''22222:''22222:''22222:''22222'))
        elif level == 1:
            display.show(Image('11111:''11111:''11111:''11111:''11111'))
    
