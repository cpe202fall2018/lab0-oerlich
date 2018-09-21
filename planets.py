def weight_on_planets():
    earthWeight = float(input("What do you weigh on earth? "))
    marsWeight = earthWeight * 0.38
    jupiterWeight = earthWeight * 2.34

    outString = "\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(marsWeight, jupiterWeight)
    print(outString)
   
   
if __name__ == '__main__':
    weight_on_planets()