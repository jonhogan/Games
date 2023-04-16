import os
import json
import requests
import fastapi
import bs4


# Create a FastAPI app instance
app = fastapi.FastAPI()

# Define a GET endpoint for saving cities data
@app.get("/save_cities")
def save_cities():
    # Send a GET request to the website that has city data
    response = requests.get("https://www.worldatlas.com/citypops.htm")

    # Check if the request was successful (status code 200)
    if response.ok:
        # Parse the HTML content of the response using BeautifulSoup
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        # Find the table element that has city data in it
        table = soup.find("table", class_="tableizer-table")
        
        # Check if the table element was found
        if table:
            # Find all the table rows that have city data in them (skip the first row which is the header)
            rows = table.find_all("tr")[1:]
            # Create an empty list to store city data as dictionaries
            cities = []
            # Loop through each row and get city data from it
            for row in rows:
                # Find all the table cells in each row
                cells = row.find_all("td")
                # Get city name, country name and population from cells and strip any whitespace or commas from them
                city_name = cells[0].text.strip()
                country_name = cells[1].text.strip()
                population = int(cells[2].text.strip().replace(",", ""))
                # Create a dictionary with city data as keys and values
                city_data = {"city": city_name, "country": country_name, "population": population}
                # Append city data dictionary to cities list
                cities.append(city_data)

            # Get the current directory where the Python script is located
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Create a file path for the JSON file in the same directory as the Python script
            file_path = os.path.join(current_dir, "fastCities.json")

            # Print the file path for debugging
            print(file_path)

            # Open the JSON file in write mode in the same directory as this Python file
            with open(file_path, "w") as f:
                # Dump cities list into the file as JSON with indentation of 4 spaces for readability
                json.dump(cities, f, indent=4)

            # Print the list of cities for debugging
            print(cities)

            # Return a success message as JSON response from this endpoint 
            return {"message": "Cities saved successfully"}
        else:
            # Return an error message as JSON response from this endpoint if table element was not found
            return {"message": "Table element not found"}
    else:
        # Return a failure message as JSON response from this endpoint if request was not successful 
        return {"message": "Request failed"}

# Start the FastAPI server
if __name__ == '__main__':
    import uvicorn
    #uvicorn.run(app, host='127.0.0.1', port=8000)

    save_cities()

