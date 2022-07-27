#Zach Gustafson
#Final Project
#COM 110
from graphicscopy import *
from random import randrange
from buttonclass import* #gives ability to use button class

def main():
    #create window
    win = GraphWin("Marketing Platform",800,800)
    win.setBackground("purple")
    title = Text(Point(400,25),"MarketPower")
    title.setSize(25)
    
    title.draw(win)
    explainTxt1 = Text(Point(400,50),"Company Name")
    explainTxt1.draw(win)
    userinput1 = Entry(Point(400,70),50)     
    
    userinput1.draw(win)
    
    
    #prompts for input boxes
    explainTxt2 = Text(Point(400,90),"Industry Name(Enter either tech., insurance, sports, biotech, or motor vehicle or if you have a new industry enter that)")
    explainTxt2.draw(win)
    userinput2 = Entry(Point(400,110),50)
    userinput2.draw(win)
    

    explainTxt3 = Text(Point(400,130),"Client Name: Last,First")
    explainTxt3.draw(win)
    userinput3 = Entry(Point(400,150),50)
    userinput3.draw(win)
    
    
    
    explainTxt4 = Text(Point(400,170),"Clients role in company")
    explainTxt4.draw(win)
    userinput4 = Entry(Point(400,190),50)
    userinput4.draw(win)
    
    
    
    explainTxt5 = Text(Point(400,210),"Value of sale in USD(has to be in numbers with no commas)")
    explainTxt5.draw(win)
    userinput5 = Entry(Point(400,230),50)
    userinput5.draw(win)
    
    
    inputButton = Button(win,Point(400,270),30,20,"white","Input")
#explanation of market power
    eXp = Text(Point(400,310),"Welcome to MarketPower! We are a marketing scout platform\n\
designed to help companies from all sizes target the right industries to maximize their sales.")
    eXp.setSize(18)
    eXp.draw(win)
    #explaining what happens if the input button is clicked
    p = win.getMouse()
    if inputButton.isClicked(p):
        compName = userinput1.getText()
        indName = userinput2.getText()
        roleName = userinput4.getText()
        CliName = userinput3.getText()
        valName = int(userinput5.getText())
        stringTest = []
        stringTest = [compName,indName,CliName,roleName,valName]
        #list of inputs created

        explainTxt1.undraw()
        explainTxt2.undraw()
        explainTxt3.undraw()
        explainTxt4.undraw()
        explainTxt5.undraw()

        userinput1.undraw()
        userinput2.undraw()
        userinput3.undraw()
        userinput4.undraw()
        userinput5.undraw()

       
        #second window
        win2 = GraphWin("Sales List Bar Graphs",800,800)
        win2.setCoords(0,0,800,800)
        win2.setBackground("purple")
        title = Text(Point(400,775),"MarketPower")
        title.setSize(25)
    #reading text file into program which has data of other sale
        #this was done so the user would only enter in one sale making it easier for them to
        #understand the bar graphs
        title.draw(win2)
        company = "Comp.txt"
        f = open(company)
        
        strText = f.readlines()
       
        
        techCompanies = []
        sportsCompanies = []
        insuranceCompanies = []
        biotechCompanies = []
        motorVehiclecomp = []

       
        
        for line in strText:
            splitLine = line.split(",")
            
            for word in splitLine:
                if word == "tech.":
                    techCompanies.append(line)
                    
                elif word == "sports":
                    sportsCompanies.append(line)
                elif word == "insurance":
                    insuranceCompanies.append(line)
                elif word == "biotech":
                    biotechCompanies.append(line)
                elif word == "motor vehicle":
                    motorVehiclecomp.append(line)
                    

        contacts = {}
        contacts = {1:techCompanies, 2:sportsCompanies, 3:insuranceCompanies, 4:biotechCompanies, 5:motorVehiclecomp} 
        #tech industry bar for graph one
        techBar = Rectangle(Point(120,400), Point(135,550))
        techBar.setFill("grey")
        techBar.draw(win2)
        TxTmessage = Text(Point(127.5,390), "Tech.")
        TxTmessage.draw(win2)
        
            
            
       
        #sports bar for graph one
        textMessage = Text(Point(162.5,390), "Sports")
        textMessage.draw(win2)
        sportsBar = Rectangle(Point(155,400), Point(170,500))
        sportsBar.setFill("grey")
        sportsBar.draw(win2)
        
        
        
        #insurance bar for graph one
        textMessage = Text(Point(197.5,390), "Ins.")
        textMessage.draw(win2)
        insBar = Rectangle(Point(190,400),Point(205,450))
        insBar.setFill("grey")
        insBar.draw(win2)
        
        
        textMessage = Text(Point(232.5,390),"BioTec.")
        textMessage.draw(win2)
        bioBar = Rectangle(Point(225,400),Point(240,450))
        bioBar.setFill("grey")
        bioBar.draw(win2)
        
        
        textMessage = Text(Point(267.5,390), "MotVeh.")
        textMessage.draw(win2)
        motBar = Rectangle(Point(260,400),Point(275,500))
        motBar.setFill("grey")
        motBar.draw(win2)
        #graph 1 labels
        x1Label = Text(Point(200,350),"Industries")
        x1Label.draw(win2)

        y2Label = Text(Point(50,550),"Occurence in Sales\n\
Contact List")
        y2Label.draw(win2)              
#create x axis    
        base_line = Rectangle(Point(100,400), Point(400,400)) 
        base_line.setFill("black")
        base_line.draw(win2)
#creates y axis
        left_line = Rectangle(Point(100,400), Point(100, 700))
        left_line.setFill("black")
        left_line.draw(win2)
#tech bar        
        bartech = Rectangle(Point(460,400),Point(475,650))
        bartech.setFill("grey")
        bartech.draw(win2)
        textmes = Text(Point(467.5,390),"Tech.")
        textmes.draw(win2)
#sports bar
        barSports = Rectangle(Point(495,400),Point(510,620))
        barSports.setFill("grey")
        barSports.draw(win2)
        textmes = Text(Point(502.5,390),"Sports")
        textmes.draw(win2)
#insurance bar
        barIns = Rectangle(Point(530,400),Point(545,470))
        barIns.setFill("grey")
        barIns.draw(win2)
        textmes = Text(Point(537.5,390),"Ins.")
        textmes.draw(win2)
#bio bar        
        barBio = Rectangle(Point(565,400),Point(580,430))
        barBio.setFill("grey")
        barBio.draw(win2)
        textmes = Text(Point(572.5,390),"Biotec.")
        textmes.draw(win2)
#motor vehicle bar                       
        barMot = Rectangle(Point(600,400),Point(615,520))
        barMot.setFill("grey")
        barMot.draw(win2)        
        textmes = Text(Point(607.5,390),"Motveh.")
        textmes.draw(win2)
        #graph 2 labels
        x2Label = Text(Point(600,350),"Industries")
        x2Label.draw(win2)
        y2Label = Text(Point(400,550),"Comparison of Rev.\n\
by Industry")
        y2Label.draw(win2)
 #x axis       
        base_line1 = Rectangle(Point(450,400), Point(750,400)) 
        base_line1.setFill("black")
        base_line1.draw(win2)
        #creates y axis
        left_line1 = Rectangle(Point(450,400), Point(450, 700))
        left_line1.setFill("black")
        left_line1.draw(win2)    
        #tech if statments for different inputs
        if indName == "tech.":
            techCompanies.append(stringTest)
            
            tecText = Text(Point(400,300),"The sale enetered below is in the Tech. industry.")
            tecText.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            print(techCompanies)

            techBar0 = Rectangle(Point(120,400), Point(135,600))
            techBar0.setFill("grey")
            techBar0.draw(win2)
            TxTmessage0 = Text(Point(127.5,390), "Tech.")
            TxTmessage0.draw(win2)
            
            bartech = Rectangle(Point(460,400),Point(475,700))
            bartech.setFill("grey")
            bartech.draw(win2)
            textmes = Text(Point(467.5,390),"Tech.")
            textmes.draw(win2)    
            
        #sport if statements for different inputs    
        elif indName == "sports":
            sportsCompanies.append(stringTest)
            tecText = Text(Point(400,300),"The sale enetered below is in the Sports industry.")
            tecText.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            print(sportsCompanies)
            
            textMessage0 = Text(Point(162.5,390), "Sports")
            textMessage0.draw(win2)
            sportsBar0 = Rectangle(Point(155,400), Point(170,550))
            sportsBar0.setFill("grey")
            sportsBar0.draw(win2)

            if valName <= 2000:
                barSports = Rectangle(Point(495,400),Point(510,670))
                barSports.setFill("grey")
                barSports.draw(win2)
                textmes = Text(Point(502.5,390),"Sports")
                textmes.draw(win2) 
            elif valName >= 2000 and valName <= 5000:
                barSports = Rectangle(Point(495,400),Point(510,710))
                barSports.setFill("grey")
                barSports.draw(win2)
                textmes = Text(Point(502.5,390),"Sports")
                textmes.draw(win2) 
            elif valName >= 5000:
                barSports = Rectangle(Point(495,400),Point(510,750))
                barSports.setFill("grey")
                barSports.draw(win2)
                textmes = Text(Point(502.5,390),"Sports")
                textmes.draw(win2) 
            #if statemtns for insurance inputs
        elif indName == "insurance":
            insuranceCompanies.append(stringTest)
            tecText = Text(Point(400,300),"The sale enetered below is in the Insurace industry.")
            tecText.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            print(insuranceCompanies)

            textMessage0 = Text(Point(197.5,390), "Ins.")
            textMessage0.draw(win2)
            insBar0 = Rectangle(Point(190,400),Point(205,500))
            insBar0.setFill("grey")
            insBar0.draw(win2)
            if valName <= 2000:
                barIns = Rectangle(Point(530,400),Point(545,500))
                barIns.setFill("grey")
                barIns.draw(win2)
                textmes = Text(Point(537.5,390),"Ins.")
                textmes.draw(win2)
            elif valName >= 2000 and valName <= 5000:
                barIns = Rectangle(Point(530,400),Point(545,565))
                barIns.setFill("grey")
                barIns.draw(win2)
                textmes = Text(Point(537.5,390),"Ins.")
                textmes.draw(win2)
            elif valname >= 5000:
                barIns = Rectangle(Point(530,400),Point(545,575))
                barIns.setFill("grey")
                barIns.draw(win2)
                textmes = Text(Point(537.5,390),"Ins.")
                textmes.draw(win2)
        #biotech if statements for different inputs        
        elif indName == "biotech":
            biotechCompanies.append(stringTest)
            tecText = Text(Point(400,300),"The sale enetered below is in the Biological Technology industry.")
            tecText.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            print(biotechCompanies)
            
            textMessage0 = Text(Point(232.5,390),"BioTec.")
            textMessage0.draw(win2)
            bioBar0 = Rectangle(Point(225,400),Point(240,500))
            bioBar0.setFill("grey")
            bioBar0.draw(win2)

            if valName <= 2000:
                barBio = Rectangle(Point(565,400),Point(580,470))
                barBio.setFill("grey")
                barBio.draw(win2)
                textmes = Text(Point(572.5,390),"Biotec.")
                textmes.draw(win2)
            elif valName >= 2000 and valName <= 5000:
                barBio = Rectangle(Point(565,400),Point(580,510))
                barBio.setFill("grey")
                barBio.draw(win2)
                textmes = Text(Point(572.5,390),"Biotec.")
                textmes.draw(win2)
            elif valName >= 5000:
                barBio = Rectangle(Point(565,400),Point(580,540))
                barBio.setFill("grey")
                barBio.draw(win2)
                textmes = Text(Point(572.5,390),"Biotec.")
                textmes.draw(win2)
         #if statements for motor vehicle       
        elif indName == "motor vehicle":
            motorVehiclecomp.append(stringTest)
            tecText = Text(Point(400,300),"The sale enetered below is in the Motor Vehicle industry.")
            tecText.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            print(motorVehiclecomp)

            textMessage0 = Text(Point(267.5,390), "MotVeh.")
            textMessage0.draw(win2)
            motBar0 = Rectangle(Point(260,400),Point(275,550))
            motBar0.setFill("grey")
            motBar0.draw(win2)

            if valName <= 2000:
                barMot = Rectangle(Point(600,400),Point(615,560))
                barMot.setFill("grey")
                barMot.draw(win2)        
                textmes = Text(Point(607.5,390),"Motveh.")
                textmes.draw(win2)
            elif valName >= 2000 and valName<= 5000:
                barMot = Rectangle(Point(600,400),Point(615,560))
                barMot.setFill("grey")
                barMot.draw(win2)        
                textmes = Text(Point(607.5,390),"Motveh.")
                textmes.draw(win2)
            elif valName >= 5000:
                barMot = Rectangle(Point(600,400),Point(615,600))
                barMot.setFill("grey")
                barMot.draw(win2)        
                textmes = Text(Point(607.5,390),"Motveh.")
                textmes.draw(win2)
         #if there is a new industry entered       
        else:
            newBar = Rectangle(Point(295,400),Point(310,450))
            newBar.setFill("grey")
            newBar.draw(win2)
            textMessage = Text(Point(302.5,390), indName)
            textMessage.draw(win2)
            lis = Text(Point(400,250),stringTest)
            lis.draw(win2)
            notes = Text(Point(400,300),"You have entered a sale from a company within a new industry!")
            notes.draw(win2)
            print(stringTest)
            if valName <= 2000: 
                barnew = Rectangle(Point(635,400),Point(650,440))
                barnew.setFill("grey")
                barnew.draw(win2)
                textMessage = Text(Point(642.5,390), indName)
                textMessage.draw(win2)
            elif valName >= 2000 and valName <=5000:
                barnew = Rectangle(Point(635,400),Point(650,465))
                barnew.setFill("grey")
                barnew.draw(win2)
                textMessage = Text(Point(642.5,390), indName)
                textMessage.draw(win2)
            elif valName >= 5000:
                barnew = Rectangle(Point(635,400),Point(650,490))
                barnew.setFill("grey")
                barnew.draw(win2)
                textMessage = Text(Point(642.5,390), indName)
                textMessage.draw(win2)
        #note telling the user to check the shell to see the contact list of industry    
        note = Text(Point(400,200), "Check the Shell to see the contact list of this industry.")
        note.draw(win2)
#quit button
        quitButton = Button(win2,Point(600,200),20,20, "orange","Quit")
        
        pt = win2.getMouse()
        if quitButton.isClicked(pt):
            win2.close()
            win.close()
        
        
        #pt = win.getMouse()
       
            #if appleButton.isClicked(pt):
        else:
            pt = win2.getMouse()
main()
        
    
            
    
