from nitron.products import Chaise, Canape, Table
chaise1 = Chaise(price=100, 
        cost =50, 
        mark ='Pepouse', 
        materiau ='Plastique', 
        couleur ='rouge', 
        dimensions = '50x50x30')

canape1= Canape(materiau = "Cuir",
         couleur = "Blanc",
         dimensions = '200x100x80',
         cost = 1000,
         price = 2000,
         mark = "OKLM")

chaise2 = Chaise(materiau = "Métal",
        couleur = "Gris",
        dimensions = '60x60x80',
        cost = 75,
        price = 150,
        mark = "PEPOUSE")

canape2= Canape(materiau = "Tissu",
         couleur = "Bleu",
         dimensions = '150x90x70',
         cost = 800,
         price = 1600,
         mark = "SIESTA")

table1 = Table(materiau = "Verre",
        couleur = "Transparent",
        dimensions = '120x60x75',
        cost = 350,
        price = 700,
        mark = "TEX")

Table2= Table(materiau = "Bois",
         couleur = "Chêne",
         dimensions = '150x80x75',
         cost = 250,
         price = 500,
         mark = "TEX")

#test=Product (10, 10 , 'mpo')

print (canape2.price)