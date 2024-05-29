# Create a simple calculator
first_num = 6   # first number value is assigned
sec_num = 2     # assigned a second number
division = first_num / sec_num
add = first_num + sec_num
sub = first_num - sec_num
mult = first_num * sec_num
print(add, sub, mult, division)


first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))
division = first_num / second_num
multi = first_num * second_num
add = first_num + second_num
sub = first_num - second_num
fdivi = first_num // second_num
mod = first_num % second_num
expo = first_num ** second_num
print("Division: ", division,"Multiplication: ",multi, "Subtraction: ", sub, "Addition: ", add,"Floor_Division: ", fdivi,"Modulus: ", mod,"Exponential: ", expo)
print("====================ATH Calculator=============-===")
print("====================Aadarsh Karki=============-===")

# Abc company has three products
# phone_price = 1800  #initializing phone price
# laptops_price = 3000  #initializing laptops price
# watch_price = 700   #initializing watch price
# airpods_price = 350   #initializing airpods price
# tv_price = 5500   #initializing television price
phone_tax_rate = 10
laptops_tax_rate = 20
watch_tax_rate = 8
airpods_tax_rate = 13
tv_tax_rate = 8

phone_sales_value = phone_price + (phone_price * phone_tax_rate / 100)
laptops_sales_value = laptops_price + (laptops_price * laptops_tax_rate / 100)
watch_sales_value = watch_price + (watch_price * watch_tax_rate / 100)
airpods_sales_value = airpods_price + (airpods_price * airpods_tax_rate / 100)
tv_sales_value = tv_price + (tv_price * tv_tax_rate / 100)
print("The sales value for phone is: ", phone_sales_value)
print("The sales value for laptop is: ", laptops_sales_value)
print("The sales value for watch is: ", watch_sales_value)
print("The sales value for airpod is: ", airpods_sales_value)
print("The sales value for tv is: ", tv_sales_value)

# Import math module to get the value of pi
import math

# To calculate the area of a circle for given radius
def calculate_circle_area(radius):
    # Using value of pi through the math module
    pi = math.pi
    # Area: pi * radius squared
    area = pi * (radius ** 2)
    return area

# For the radius
radius = float(input("Enter the radius of the circle: "))

# Area of the circle
area = calculate_circle_area(radius)

# Displaying result
print(f"The area of the circle is: {area}")

