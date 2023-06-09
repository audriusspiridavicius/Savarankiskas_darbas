from antra.Rectangle import Rectangle
from functions.functions import format_number
import logging
logging.basicConfig(filename="app_logs.log", encoding="UTF-8", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

def get_data():
    input_width = input("Please enter rectangle width: ")
    input_length = input("Please enter rectangle length: ")

    rec_width = format_number(input_width)
    rec_length = format_number(input_length)

    rectangle = Rectangle(rec_width, rec_length)

    area = rectangle.area()
    perimeter = rectangle.perimeter()
    logging.info(f"width = {rec_width}, length = {rec_length}, perimeter = {perimeter}, area = {area}")
    return area,perimeter


area, perimeter = get_data()

print(f"area = {area}")
print(f"perimeter = {perimeter}")