################
# DIGITSPORES #
################
# by Tristan Da Cunha
# https://github.com/TristanDaCunhaX
# Artworks generated with this script are licensed under CC BY-NC-SA 4.0

# Modules
import math
from colorsys import hls_to_rgb
# from datetime import datetime


# Global setting
totalFiles = 2000

quickFactor = 1 #to reduce filesize and export time / for debug only
seconds = 3
fps = 30
frames = seconds * fps
canvasSize = 2048 /quickFactor

thrRARE = 1/100
thrUNCOMMON = 25/100


# Style Functions

def bodyStyle():
    fill(*bodyColor)
    strokeWidth(strokeW)
    stroke(*bodyStrokeColor)

def tentacleStyle():
    stroke(*tentacleColor)
    strokeWidth(strokeW*2)
    fill(None)
    
def peripheralStyle():
    stroke(*peripheralStrokeColor)
    strokeWidth(strokeW)
    fill(*peripheralColor)




# Instructions for the whole collection

open('export/cryptospores-metadata.txt', mode='x').close() #mode 'x' prevents overwriting
for fileNumber in range(totalFiles):
    newDrawing()    # reset the drawing stack to a clear and empty stack


#Instructions for each single item in the collection

    #Item Extractions
    extractSwing = random()
    extractTopTorsion = random()
    extractBottomTorsion = random()
    extractTonnage = random()
    extractLength = random()
    extractBodyShape = random()
    extractLimbs = random()
    extractTentacleShape = random()
    extractPalette = randint(0,3)

    #Item Variables

    #Swing
    if extractSwing <= thrRARE:
        swingAngle = 360
        swingLabel = 'somersault'
    elif extractSwing <= thrUNCOMMON:
        swingAngle = randint(60,90)
        swingLabel = 'strong oscillation'
    else:
        swingAngle = randint(0,15)
        swingLabel = 'weak oscillation'

    #Head Torsion
    if extractTopTorsion <= thrRARE:
        topSpin = randint(190,220)
        topSpinLabel = 'fast'
    elif extractTopTorsion <= thrUNCOMMON:
        topSpin = randint(90,135)
        topSpinLabel = 'medium'
    else:
        topSpin = randint(15,60)
        topSpinLabel = 'slow'
    
    #Tail Torsion
    if extractBottomTorsion <= thrRARE:
        bottomSpin = randint(180,225)
        bottomSpinLabel = 'fast'
    elif extractBottomTorsion <= thrUNCOMMON:
        bottomSpin = randint(90,135)
        bottomSpinLabel = 'medium'
    else:
        bottomSpin = randint(15,60)
        bottomSpinLabel = 'slow'
    
    #Tonnage
    if extractTonnage <= thrRARE:
        tonnage = int(canvasSize / 10)
        tonnageLabel = 'xs'
    elif extractTonnage <= thrUNCOMMON:
        tonnage = int(canvasSize / 7)
        tonnageLabel = 'sm'
    elif extractTonnage >= 1-thrRARE:
        tonnage = int(canvasSize / 1.5)
        tonnageLabel = 'xl'
    elif extractTonnage >= 1-thrUNCOMMON:
        tonnage = int(canvasSize / 3)
        tonnageLabel = 'lg'
    else:
        tonnage = int(canvasSize / randint(4,6))
        tonnageLabel = 'md'
    
    #Length (how many "worm rings"?)
    if extractLength <= thrRARE:
        nShapes = randint(10,20)
        shDist = canvasSize/128
        howFrequentLimbs = 5
        lengthLabel = 'xs'
    elif extractLength <= thrUNCOMMON:
        nShapes = randint (40,60)
        shDist = canvasSize/192
        howFrequentLimbs = 7
        lengthLabel = 'sm'
    elif extractLength >= 1-thrRARE:
        nShapes = randint (180,200)
        shDist = canvasSize/128
        howFrequentLimbs = 13
        lengthLabel = 'xl'
    elif extractLength >= 1-thrUNCOMMON:
        nShapes = randint (140,160)
        shDist = canvasSize/192
        howFrequentLimbs = 12
        lengthLabel = 'lg'
    else:
        nShapes = randint (90,110)
        shDist = canvasSize/256
        howFrequentLimbs = 10
        lengthLabel = 'md'
    
    #Body shape
    if extractBodyShape <= thrRARE:
        bodyShapeLabel = 'none'
    elif extractBodyShape <= thrUNCOMMON:
        bodyShapeLabel = 'pyramid'
    elif extractBodyShape >= 1-thrRARE:
        bodyShapeLabel = 'double fuse'
    elif extractBodyShape >= 1-thrUNCOMMON:
        bodyShapeLabel = 'fuse'
    else:
        bodyShapeLabel = 'cube'
        
    #Limbs
    if extractLimbs <= thrRARE:
        howManyLimbs = 2
    elif extractLimbs <= thrUNCOMMON:
        howManyLimbs = 8
    else:
        howManyLimbs = 4
   
    #Tentacle shape
    if extractTentacleShape <= thrRARE:
        tentacleShapeLabel = 'leaf'
    elif extractTentacleShape <= thrUNCOMMON:
        tentacleShapeLabel = 'arc'
    else:
        tentacleShapeLabel = 'line'

    #Peripherals shape
    
    
    #Palettes

    #Palette #0 Abyss    
    if extractPalette == 0:
        paletteLabel = 'abyss'
        
        #bgColor
        hh = randint(210,240)
        ll = randint(0,20)
        ss = randint(70,100)
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bgColor = rr,gg,bb,1
        
        #bodyColor
        hh = randint(210,240)
        ll = randint(60,90)
        ss = randint(0,100)
        alpha = .15
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bodyColor = rr,gg,bb,alpha
    
        #tentacleColor
        hh = hh
        ll = ll + randint(-20,20)
        ss = ss + randint(-10,10)
        alpha = 1
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        tentacleColor = rr,gg,bb,alpha
        
        bodyStrokeColor = bgColor
        peripheralColor = bodyColor
        peripheralStrokeColor = tentacleColor
    #end palette #0

    #Palette #1 Blaze
    if extractPalette == 1:    
        paletteLabel = 'blaze'
        
        #bgColor
        hh = randint(-30,0)
        if hh < 0:
            hh = 360 + hh
        ll = randint(15,35)
        ss = randint(70,90)
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bgColor = rr,gg,bb,1
        
        #bodyColor
        hh = randint(20,40)
        ll = randint(60,90)
        ss = 100
        alpha = .1
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bodyColor = rr,gg,bb,alpha
    
        #tentacleColor
        hh = hh - randint(20,40)
        if hh < 0:
            hh = hh + 360
        ll = randint(60,80)
        ss = 100
        alpha = .75
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        tentacleColor = rr,gg,bb,alpha
        
        bodyStrokeColor = tentacleColor
        peripheralColor = tentacleColor
        peripheralStrokeColor = tentacleColor
    #end palette #1
    
    #Palette #2 Celestial    
    if extractPalette == 2:
        paletteLabel = 'celestial'
        
        #bgColor
        hh = randint(200,230)
        ll = randint(60,80)
        ss = randint(50,70)
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bgColor = rr,gg,bb,1
        
        #bodyColor
        hh = randint(280,330)
        ll = randint(85,100)
        ss = randint(85,100)
        alpha = .08
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bodyColor = rr,gg,bb,alpha
    
        #tentacleColor
        hh = hh + randint(0,20)
        ll = ll + randint(-50,-30)
        ss = ss + randint(0,20)
        alpha = .7
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        tentacleColor = rr,gg,bb,alpha
        
        bodyStrokeColor = tentacleColor
        peripheralColor = bodyColor
        peripheralStrokeColor = tentacleColor
    #end palette #2

    #Palette #3 Dawn    
    if extractPalette == 3:
        paletteLabel = 'dawn'
        
        #bgColor
        hh = randint(140,170)
        ll = randint(35,55)
        ss = randint(80,100)
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bgColor = rr,gg,bb,1
        
        #bodyColor
        hh = randint(60,90)
        ll = randint(70,80)
        ss = randint(0,50)
        alpha = .2
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        bodyColor = rr,gg,bb,alpha
    
        #tentacleColor
        hh = hh
        ll = randint(10,30)
        ss = randint(40,60)
        alpha = .6
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        tentacleColor = rr,gg,bb,alpha

        #peripheralColor
        hh = hh + randint(0,20)
        ll = randint(60,90)
        ss = randint(90,100)
        alpha = .25
        rr,gg,bb = hls_to_rgb(hh/360,ll/100,ss/100)
        peripheralColor = rr,gg,bb,alpha

        
        bodyStrokeColor = tentacleColor
        peripheralStrokeColor = tentacleColor
    #end palette #3
    
    #Stroke width
    strokeW = canvasSize/512



    # Start drawing with previous settings
    for eachFrame in range(frames):
    
        # Set new frame, canvas, background and center origin
        newPage(canvasSize, canvasSize)
        frameDuration(1/fps)
        fill(*bgColor)
        rect(0, 0, canvasSize, canvasSize)
    
        # Set current Swing state
        translate(canvasSize/2, canvasSize/2)
        if extractSwing <= thrRARE:
            rotate(360 * eachFrame/frames) # somersault
        else:
            rotate(swingAngle * sin(eachFrame/frames * 2*pi)) # oscillation
        startingOrientation = extractSwing*360
        rotate(startingOrientation) #basic orientation

        # Center the overall composition                   
        translate(0, - nShapes*shDist/2)
        if bodyShapeLabel == 'pyramid': 
            translate(0, tonnage/4) #optical compenation for pyramids

        # Set current Torsion state
        bottomAngle = bottomSpin * sin(eachFrame/frames * 2*pi)
        topAngle = topSpin * cos(eachFrame/frames * 2*pi)
    
        # Draw all the shapes in the current state
        for i in range(nShapes):
            ff = i / nShapes
            save()
            translate(0, i * shDist)
            scale(1, 2/3)                        # perspective distortion
            rotate(bottomAngle + ff*(topAngle - bottomAngle))
            
            #Define change factor for tentacles' length based on body shape
            if (bodyShapeLabel == 'fuse') or (bodyShapeLabel == 'double fuse'): #fuse or double fuse
                changeFactor = sin(ff*pi)
            elif bodyShapeLabel == 'pyramid':
                changeFactor = 1-ff
            else: #none or cube
                changeFactor = 1
            
            #Draw Tentacles and Peripherals
            if i%howFrequentLimbs == 0:
                for jj in range(howManyLimbs):
                    rotate(jj/howManyLimbs * 360)
                    
                    endPoint = tonnage/3*2 * changeFactor + tonnage/3
                    
                    #Tentacles
                    tentacleStyle()                    
                    tentacle = BezierPath()
                    if tentacleShapeLabel == 'leaf':
                        tentacle.arc((-endPoint,0), endPoint, 90,0,'clockwise')
                        tentacle.arc((0,endPoint), endPoint, 270,180,'clockwise')
                    elif tentacleShapeLabel == 'arc':
                        tentacle.arc((-endPoint,0), endPoint, 90,0,'clockwise')
                    else: #line
                        tentacle.line((0,0),(endPoint,-endPoint))
                    drawPath(tentacle)
                    
                    #Peripherals
                    peripheralStyle()
                    oval(endPoint - tonnage/12, - endPoint - tonnage/12, tonnage/6, tonnage/6)
            
            
            # Draw Body  
            bodyStyle()      
            if bodyShapeLabel == 'none':
                pass
            elif bodyShapeLabel == 'double fuse':
                if i%2==0:
                    rotate(90)
                oval(-tonnage/2*sin(ff*2*pi), -tonnage/4*sin(ff*2*pi), tonnage*sin(ff*2*pi), tonnage/2*sin(ff*2*pi))
            elif bodyShapeLabel == 'fuse':
                oval(-tonnage/2*changeFactor, -tonnage/4*changeFactor, tonnage*changeFactor, tonnage/2*changeFactor)
            elif bodyShapeLabel == 'pyramid':
                rect(-tonnage/2*changeFactor, -tonnage/2*changeFactor, tonnage*changeFactor, tonnage*changeFactor)
            else:
                rect(-tonnage/4, -tonnage/4, tonnage/2, tonnage/2)
        
            restore()
        
    # now = datetime.now()
    
    saveImage(f'export/digitspore-{fileNumber:0>4}.mp4')
    
    # Write metadata to .txt file
    with open('export/cryptospores-metadata.txt', mode='a', encoding='utf-8') as txtFile:
        txtFile.write(f'"{fileNumber:0>4}": {chr(123)}\n')
        # TRAITS
        txtFile.write(f'       "traits": {chr(123)}\n')
        txtFile.write(f'              "swing": "{swingLabel}",\n')
        txtFile.write(f'              "head spin": "{topSpinLabel}",\n')
        txtFile.write(f'              "tail spin": "{bottomSpinLabel}",\n')    
        txtFile.write(f'              "tonnage": "{tonnageLabel}",\n')
        txtFile.write(f'              "length": "{lengthLabel}",\n')
        txtFile.write(f'              "body shape": "{bodyShapeLabel}",\n')
        txtFile.write(f'              "limbs": "{howManyLimbs}",\n')
        txtFile.write(f'              "tentacle shape": "{tentacleShapeLabel}",\n')
        txtFile.write(f'              "palette": "{paletteLabel}",\n')
        txtFile.write('              },\n') # END TRAITS
        # INPUTS
        txtFile.write(f'       "inputs": {chr(123)}\n')
        txtFile.write(f'              "swingAngle": "{swingAngle}",\n')
        txtFile.write(f'              "startingOrientation": "{startingOrientation}",\n')
        txtFile.write(f'              "topSpin": "{topSpin}",\n')
        txtFile.write(f'              "bottomSpin": "{bottomSpin}",\n')
        txtFile.write(f'              "tonnage": "{tonnage}",\n')
        txtFile.write(f'              "nShapes": "{nShapes}",\n')
        txtFile.write(f'              "bodyShapeLabel": "{bodyShapeLabel}",\n')
        txtFile.write(f'              "howManyLimbs": "{howManyLimbs}",\n')
        txtFile.write(f'              "tentacleShapeLabel": "{tentacleShapeLabel}",\n')
        txtFile.write(f'              "extractPalette": "{extractPalette}",\n')
        txtFile.write(f'              "bgColor": "{bgColor}",\n')
        txtFile.write(f'              "bodyColor": "{bodyColor}",\n')
        txtFile.write(f'              "tentacleColor": "{tentacleColor}",\n')
        txtFile.write(f'              "peripheralColor": "{peripheralColor}"\n')
        txtFile.write('              }\n') # END INPUTS
    
        txtFile.write('       },\n')
        txtFile.write('\n')
    
    newDrawing()    # reset drawing

#END
