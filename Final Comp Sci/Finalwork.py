def main():
    company = "Comp.txt"
    f = open(company)
    
    strText = f.readlines()
    #print(strText)
    
    techCompanies = []
    sportsCompanies = []
    insuranceCompanies = []
    biotechCompanies = []
    motorVehiclecomp = []
    
    
    for line in strText:
        splitLine = line.split(",")
        #print(splitLine)
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
                
##    print(techCompanies)
##    print(sportsCompanies)
##    print(insuranceCompanies)
##    print(biotechCompanies)
##    print(motorVehiclecomp)

    contacts = {}
    contacts = {1:techCompanies, 2:sportsCompanies, 3:insuranceCompanies, 4:biotechCompanies, 5:motorVehiclecomp} 
    #print(contacts)
    
main()
