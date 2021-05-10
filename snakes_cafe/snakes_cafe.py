print("""
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")


orders = [
    {
        "Appetizers": [
          "Wings",
         "Cookies",
          "Spring Rolls",
        ],
    },
    {
      "Entrees": [
          "Salmon",
          "Steak",
        "Meat Tornado",
        "A Literal Garden",
        ],
    },
     {
      "Desserts": [
          "Ice Cream",
          "Cake",
          "Pie",
        ],
    },
     {
      "Drinks": [
         "Coffee",
         "Tea",
        "Unicorn Tears",
        ],
    },
]
count=0
order = " "
while order != "exit":
 order=input("""***********************************
 ** What would you like to order? **
 ***********************************
 >""")  
 count+=1
 print(f"** {count} order of {order} have been added to your meal **")

