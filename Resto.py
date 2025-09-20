#Multiline string print

print("Welcome to my restaurant")
Todays_special = """
                 ON DISPLAY
                 1. Varan Bhat khiachadi with ghee
                 2. shrikhand Thali
                 3. Thali pith 
                 4. Poha 
                """
print("Todays special menu %s" %(Todays_special))

if "Varan Bhat khiachadi with ghee" in Todays_special:
    print("Client ordered Varan Bhat khiachadi with ghee")

if "shrikhand Thali" in Todays_special:
    print("Client ordered shrikhand Thali")

if "Thali pith" in Todays_special:
    print("Client ordered Thali pith")

if "Poha" in Todays_special:
    print("Client ordered Poha")

Menu_list = """
            1. Varan bhat with ghee
            2. Thali pith (kakadi + onion) with curd and salad
            3. Poha with coconut Highly Fiber added Poha with raw cocunt
            4. pickles
            5. Sevaya Upama
            6. Chapati with shrikhand with added papad, aloo ki sabji
"""

print("For detail information click below link") 