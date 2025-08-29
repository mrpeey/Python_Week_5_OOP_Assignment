# Activity 1 

# Base class representing a Book
class Book:
    def __init__(self, title, author, published_year, available_copies):
        self.title = title
        self.author = author
        self.published_year=published_year
        self.available_copies = available_copies
    
    def get_description(self):
        return f" The book,'{self.title}', by {self.author} was published in {self.published_year}"
    
    def check_out(self):
        if self.available_copies> 0:
            self.available_copies -= 1
            return f"We had {self.available_copies + 1} book copies in library. One copy of '{self.title}' checked out. Copies left: {self.available_copies}."
        else:
            return f"The '{self.title}' is not currently available."

    def check_in(self):
        self.available_copies += 1
        return f"One copy of '{self.title}' checked in. Copies available: {self.available_copies}."

# Derived class for EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, published_year, pages, format):
        super().__init__(title, author, published_year, available_copies=None)
        self.pages = pages
        self.format = format
    
    # Override to reflect unlimited availability for eBooks
    def check_out(self):
        return f"'{self.title}' is an eBook and can be downloaded anytime with Kindle App."
    
    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} - Number of Pages: {self.pages} Pages, Format: {self.format}."


book1 = Book("Flood of Tears", "Poulo Paulus Poulo", 2016, 10)
ebook1 = EBook("The Great Story of Endurance", "Poulo Poulo", 2015, 117, "Kindle Format")

print(book1.get_description())
print(book1.check_out())
print(book1.check_in())
print(book1.check_out())
print(book1.check_out())

print(ebook1.get_description())
print(ebook1.check_out())

# Activity 2

# Base class Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Derived class Car inherits from Base class Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class Plane inherits from Base class Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived class Boat inherits from Base class Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
for vehicle in (car, plane, boat):
    vehicle.move()