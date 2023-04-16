import base64
import tkinter as tk
from geopy.geocoders import Nominatim
import folium
import webbrowser
from io import BytesIO
from PIL import Image, ImageTk
from selenium import webdriver

# create the main window
root = tk.Tk()

# create a label and an entry widget for the city name
label = tk.Label(root, text='Enter City Name:')
label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# create a button widget for generating the map
button = tk.Button(root, text='Generate Map')
button.pack()

# create a label for displaying the map image
map_label = tk.Label(root)
map_label.pack()

def generate_map():
    # get the city name from the entry widget
    city = city_entry.get()

    # geocode the city name to latitude and longitude coordinates
    geolocator = Nominatim(user_agent='my_app')
    location = geolocator.geocode(city)
    latitude, longitude = location.latitude, location.longitude

    # generate a map of the area
    m = folium.Map(location=[latitude, longitude], zoom_start=13)

    # Render the map to an image using selenium
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(800, 600)
    html = m.get_root().render()
    encoded_html = base64.b64encode(html.encode('utf-8')).decode('utf-8')
    driver.get("data:text/html;base64," + encoded_html)
    png_data = BytesIO(driver.get_screenshot_as_png())
    png = png_data.getvalue()
    driver.quit()

    # Display the map image in the GUI
    img = Image.open(BytesIO(png))
    img.thumbnail((800, 600))
    img_tk = ImageTk.PhotoImage(img)
    map_label.config(image=img_tk)
    map_label.image = img_tk

# bind the button widget to the function
button.config(command=generate_map)

# start the GUI loop
root.mainloop()
