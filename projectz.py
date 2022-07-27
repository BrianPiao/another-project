import pandas as p
df = p.read_csv("https://raw.githubusercontent.com/whitehatjr/c-129-project/main/Processed_data/final_data.csv")
#df.drop(["Unnamed:0"], axis = 1,inplace = True)


df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()

grav = []
#converting solar mass and radius into km & kg
def convert(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] *= 6.957e+8
        mass[i] *= 1.989e+30
convert(radius,mass)

def gravcalc(radius,mass):
    G = 6.674e-11
    for e in range(0,len(mass)):
        g = (mass[e]*G)/((radius[e])**2)
        grav.append(g)
gravcalc(radius,mass)
df["Gravity"] = grav
df.to_csv("stargrav.csv")