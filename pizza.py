import random

# Lists of options for different pizza components
sizes = ['25 cm', '28 cm', '32 cm']
crusts = ['Classic', 'Cheese']
sauces = ['BBQ', 'Korean BBQ', 'Sauce Hollandaise', 'Tomatensoße', 'keine Soße']
toppings = ['Ananas', 'Bacon', 'Basilikum-Pesto','Blattspinat','Brokkoli','Burger-Sauce','Champignons',
            'Cherrytomaten','Chillisalami','Curry-Sauce', 'Dänische Remoulade', 'Frühlingszwiebeln','Gurke (dänisch)',
            'Gyros','Hirtenkäse','Hähnchenbrust','Italienischer Hartkäse','Jalapeneos','Knoblauch in Öl','Käse (Mozzarella)',
            'Mais','Mozzarella Kugeln','Oliven (grün)','Paprika','Pfifferlinge','Pizza Chillis','Prosciutto Cotto',
            'Pulled Beef', 'Rinderhack', 'Rindersteakstreifen', 'Röstzwiebeln', 'Salami', 'Sesam', 'Spargel (grün)',
            'Steakpfeffer', 'Sucuk', 'Teriyaki Sauce', 'Thunfisch', 'Tomaten', 'Tomaten-Ketchup', 'Tsatsiki',
            'Vegane Filetstreifen', 'Vegane Sauce', 'Veganer Reibeschmelz', 'Würstchen', 'Zwiebeln (rot)']


def generate_random_pizza():
    size = random.choice(sizes)
    crust = random.choice(crusts)
    sauce = random.choice(sauces)

    # Choose a random number of toppings (between 1 and 4)
    num_toppings = random.randint(1, 4)
    chosen_toppings = random.sample(toppings, num_toppings)

    return {
        'Size': size,
        'Crust': crust,
        'Sauce': sauce,
        'Toppings': chosen_toppings
    }


def main():
    print("Willkommen beim Pizzagenerator")
    num_pizzas = int(input("Wie viele Pizzen sollen erzeugt werden? ").strip())

    for i in range(num_pizzas):
        pizza = generate_random_pizza()
        print("\nPizza {}: ".format(i + 1))
        print("Größe: {}".format(pizza['Size']))
        print("Kruste: {}".format(pizza['Crust']))
        print("Soße: {}".format(pizza['Sauce']))
        print("Belag: {}".format(', '.join(pizza['Toppings'])))


if __name__ == "__main__":
    main()

