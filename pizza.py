import random

# Lists of options for different pizza components
größen = ['25 cm', '28 cm', '32 cm']
krusten = ['Klassik', 'Käse']
sauces = ['BBQ', 'Korean BBQ', 'Sauce Hollandaise', 'Tomatensoße', 'keine Soße']
toppings = ['Ananas', 'Bacon', 'Basilikum-Pesto','Blattspinat','Brokkoli','Burger-Sauce','Champignons',
            'Cherrytomaten','Chillisalami','Curry-Sauce', 'Dänische Remoulade', 'Frühlingszwiebeln','Gurke (dänisch)',
            'Gyros','Hirtenkäse','Hähnchenbrust','Italienischer Hartkäse','Jalapeneos','Knoblauch in Öl','Käse (Mozzarella)',
            'Mais','Mozzarella Kugeln','Oliven (grün)','Paprika','Pfifferlinge','Pizza Chillis','Prosciutto Cotto',
            'Pulled Beef', 'Rinderhack', 'Rindersteakstreifen', 'Röstzwiebeln', 'Salami', 'Sesam', 'Spargel (grün)',
            'Steakpfeffer', 'Sucuk', 'Teriyaki Sauce', 'Thunfisch', 'Tomaten', 'Tomaten-Ketchup', 'Tsatsiki',
            'Vegane Filetstreifen', 'Vegane Sauce', 'Veganer Reibeschmelz', 'Würstchen', 'Zwiebeln (rot)']

def main():
    num_pizzas = eingabe()
    pizza_schleife(num_pizzas)

def eingabe():
    print("Willkommen beim Pizzagenerator")
    return int(input("Wie viele Pizzen sollen erzeugt werden?").strip())

def pizza_schleife(num_pizzas):
    for i in range(num_pizzas):
        pizza = zufalls_pizza()
        print("\nPizza {}: ".format(i + 1))
        print("Größe: {}".format(pizza['Größe']))
        print("Kruste: {}".format(pizza['Kruste']))
        print("Soße: {}".format(pizza['Sauce']))
        print("Belag: {}".format(', '.join(pizza['Toppings'])))

def zufalls_pizza():
    größe = random.choice(größen)
    kruste = random.choice(krusten)
    sauce = random.choice(sauces)

    # Choose a random number of toppings (between 1 and 4)
    num_toppings = random.randint(1, 4)
    chosen_toppings = random.sample(toppings, num_toppings)

    return {
        'Größe': größe,
        'Kruste': kruste,
        'Sauce': sauce,
        'Toppings': chosen_toppings
    }



if __name__ == "__main__":
    main()

