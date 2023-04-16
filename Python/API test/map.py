import gmplot
import sys
from geopy.geocoders import Nominatim
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from keys.keys import gMapKey

# Replace YOUR_API_KEY with your actual Google Maps API key
api_key = gMapKey


# Function to get the coordinates of a city
def get_city_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_map")
    location = geolocator.geocode(city_name)
    return location.latitude, location.longitude

# Function to create and display the map
def display_map():
    city_name = city_input.text()

    # Get the coordinates of the city
    latitude, longitude = get_city_coordinates(city_name)

    # Create the map centered at the city coordinates
    gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13, apikey=api_key)

    # Add a marker at the city coordinates
    gmap.marker(latitude, longitude, title=city_name)

    # Generate the HTML file with the map
    map_file = "city_map.html"
    gmap.draw(map_file)

    # Load the generated HTML file into the QWebEngineView widget
    view.load(QUrl.fromLocalFile(map_file))

# Create the PyQt5 application
app = QApplication(sys.argv)

# Create the main window and layout
window = QWidget()
window.setWindowTitle("City Map")
layout = QVBoxLayout()

# Create the city input field and display button
city_input = QLineEdit()
display_button = QPushButton("Display Map")
display_button.clicked.connect(display_map)

# Create the QWebEngineView widget
view = QWebEngineView()

# Add the widgets to the layout
layout.addWidget(city_input)
layout.addWidget(display_button)
layout.addWidget(view)

# Set the window layout and show the window
window.setLayout(layout)
window.show()

# Start the PyQt5 event loop
sys.exit(app.exec_())