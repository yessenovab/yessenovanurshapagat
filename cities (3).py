from tkinter import *
#Graphical user interface (GUI) means all those windows, buttons, text fields for input that you see on the screen
# when you open an application.
from geopy.geocoders import Nominatim
#It uses geopy library to get lattitude and longitude from postal codes
import math
#used in code for complex mathematical calculations

#Then uses Haversine formula to calculate distance from those
def calculateDistance(z1, z2):
    R = 6371

    geolocator = Nominatim(user_agent="myAPP")

    location1 = geolocator.geocode(z1 + " KZ")

    location2 = geolocator.geocode(z2 + " KZ")

    lat_diff = location1.latitude - location2.latitude
    long_diff = location1.longitude - location2.longitude

    t1 = math.sin(lat_diff/2)**2 + math.cos(location1.latitude) * math.cos(location2.latitude) * math.sin(long_diff/2)**2
    t = math.atan2(math.sqrt(t1), math.sqrt(1-t1))

    return 2 * R * t

# create a label and immediately place
#we have created a label (tag) with text.
class Frames:
    def take_input(self):
        Label(root, text="Enter city 1 postal code: ", font=("Arial Bold", 20)).grid(row=0, column=0, padx=25, pady=25)
        self.city1 = Text(root, height=1, width=10, font=("Arial Bold", 20))
        self.city1.grid(row=0, column=1, padx=25, pady=25)

        Label(root, text="Enter city 2 postal code: ", font=("Arial Bold", 20)).grid(row=1, column=0, padx=25, pady=25)
        self.city2 = Text(root, height=1, width=10, font=("Arial Bold", 20))
        self.city2.grid(row=1, column=1, padx=25, pady=25)

        Button(root, text="Get Distance!", font=("Arial Bold", 15),
               command=lambda: [self.get_result(), root.withdraw()]).grid(row=2, padx=25, pady=25)

    # we subclassed Toplevel and kept the new window related things together in that class.
    def get_result(self):
        newwin = Toplevel(root)
        newwin.title('Result')

        zip1 = self.city1.get("1.0", "end-1c")
        zip2 = self.city2.get("1.0", "end-1c")

        distance = calculateDistance(zip1, zip2)
        distance = round(distance, 2)

        Label(newwin, text="The distance between the two cities is: ", font=("Arial Bold", 20)).grid(padx=25, pady=25)
        Label(newwin, text=f"{distance} km", font=("Arial Bold", 20)).grid(padx=25, pady=25)


# window drawing loop
root = Tk()
app = Frames()
app.take_input()
root.mainloop()
