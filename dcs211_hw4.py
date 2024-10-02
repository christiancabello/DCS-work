import requests
import json 
import time


#! function must take a json file containing a USGS dictionary 
#! prints a human-friendly output of time, date, magnitude, and location of all earthquakes given in the JSON, like shown below 
def readAndPrintQuakes(json_file: str) -> None:  
    '''
        definition: this function takes a json file containing a USGS dictionary
        as a parameter and returns the file as a human friendly output of the data 
    
        parameters: 
            json_file: str object with the USGS dictionary information 
        
        returns:  
            the data as an output of time, date, magnitude, and location of the 
            earthquakes in an easy to read format 
    '''
    with open(json_file, 'r') as infile: 
        data = json.load(infile) 
    
    for quakes in data['features']:  
        properties = quakes['properties'] 
        quake_time = (properties['time'] // 1000) 
        quake_timescript = time.strftime("%H:%M:%S on %a, %d %b %Y", time.gmtime(quake_time)) 
        quake_magnitude = properties['mag']
        quake_location = properties['place']
        printResult(quake_timescript, quake_magnitude, quake_location)

def fetchAndPrintQuakes(start_date: str, end_date: str, min_magnitude: float) -> None:  
    '''
        definition: this function takes a start date, end date, and a minimum 
        earthquake magnitude as parameters and utilizes requests to find all 
        matches within the provided URL
        
        parameters: 
            start_date: a string corresponding to the starting period to look for earthquakes
            end_date: a string corresponding to the ending period to look for earthquakes
            min_magnitude: a float object corresponding to the smallest possible magnitude
        
        returns: 
            None
    '''
    params = {
        "format": "geojson",
        "starttime": start_date,
        "endtime": end_date, 
        "minmagnitude": min_magnitude   
    }
    my_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"  
    my_result = requests.get(my_url, params = params) 
    if my_result.status_code == 200: 
        data = my_result.json() 
        for quakes in data['features']:  
            properties = quakes['properties'] 
            quake_time = (properties['time'] // 1000) 
            quake_timescript = time.strftime("%H:%M:%S on %a, %d %b %Y", time.gmtime(quake_time)) 
            quake_magnitude = properties['mag']
            quake_location = properties['place']
            printResult(quake_timescript, quake_magnitude, quake_location)
    
def printResult(quake_timescript: str, quake_magnitude: float, quake_location: str) -> None:  
    '''
        definition: this function takes the parameters quake_timescript, quake_magnitude,
        and quake_location and returns a sentence composed of all the imformation provided 
        
        parameters: 
            quake_timescript: a string object corresponding to time of the earthquake 
            quake_magnitude: a float object corresponding to magnitude of the earthquake 
            quake_location: a string object corresponding to the location of the earthquake 
        
        returns: 
            a readable sentence version of the parameters
    
    
    '''
    print(f"At {quake_timescript}: earthquake of magnitude {quake_magnitude} at {quake_location}")
    
    
def main() -> None: 
    null = None 
    quake_data = {"type":"FeatureCollection","metadata":{"generated":1727823630000,"url":"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=5.4&starttime=2024-09-25&endtime=2024-09-30","title":"USGS Earthquakes","status":200,"api":"1.14.1","count":2},"features":[{"type":"Feature","properties":{"mag":6.3,"place":"Mauritius - Reunion region","time":1727378368811,"updated":1727464919721,"tz":null,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/us7000ngmr","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000ngmr&format=geojson","felt":null,"cdi":null,"mmi":0,"alert":"green","status":"reviewed","tsunami":0,"sig":611,"net":"us","code":"7000ngmr","ids":",usauto7000ngmr,at00skfpoj,pt24270000,us7000ngmr,","sources":",usauto,at,pt,us,","types":",internal-moment-tensor,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,","nst":101,"dmin":3.949,"rms":0.83,"gap":29,"magType":"mww","type":"earthquake","title":"M 6.3 - Mauritius - Reunion region"},"geometry":{"type":"Point","coordinates":[66.5466,-17.1899,10]},"id":"us7000ngmr"},
    {"type":"Feature","properties":{"mag":5.5,"place":"28 km SSE of Akkeshi, Japan","time":1727334070361,"updated":1727420876610,"tz":null,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/us7000ngi1","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000ngi1&format=geojson","felt":2,"cdi":2.7,"mmi":4.74,"alert":"green","status":"reviewed","tsunami":0,"sig":466,"net":"us","code":"7000ngi1","ids":",us7000ngi1,usauto7000ngi1,","sources":",us,usauto,","types":",dyfi,internal-moment-tensor,losspager,moment-tensor,origin,phase-data,shakemap,","nst":133,"dmin":1.607,"rms":0.77,"gap":36,"magType":"mww","type":"earthquake","title":"M 5.5 - 28 km SSE of Akkeshi, Japan"},"geometry":{"type":"Point","coordinates":[145.0395,42.8149,57.887]},"id":"us7000ngi1"}],"bbox":[66.5466,-17.1899,10,145.0395,42.8149,57.887]}
    with open("data_json", "w") as outfile: 
        json.dump(quake_data, outfile) 
    
    print(f"Testing the function readAndPrintQuakes: ") 
    print('\t')
    print(f"Actual:")
    readAndPrintQuakes("data_json") 
    print('\t')
    print("Expected:")
    print("At 19:19:28 on Thu, 26 Sep 2024: earthquake of magnitude 6.3 at Mauritius - Reunion region")
    print("At 07:01:10 on Thu, 26 Sep 2024: earthquake of magnitude 5.5 at 28 km SSE of Akkeshi, Japan")
    print('\t')

    print("Testing the function fetchAndPrintQuakes: ")
    print('\t')
    print(f"Actual:")
    fetchAndPrintQuakes("2023-10-01", "2023-10-03", 5.0)
    print('\t')
    print(f"Expected:")
    print("At 14:17:57 on Mon, 02 Oct 2023: earthquake of magnitude 5 at Izu Islands, Japan region")
    print("At 14:03:39 on Mon, 02 Oct 2023: earthquake of magnitude 5.3 at 52 km SSE of Karakenja, Tajikistan")
    print("At 08:58:37 on Mon, 02 Oct 2023: earthquake of magnitude 5.3 at 189 km WSW of Nabire, Indonesia")
    print("At 02:33:43 on Mon, 02 Oct 2023: earthquake of magnitude 5 at Bonin Islands, Japan region")
    print("At 02:06:10 on Mon, 02 Oct 2023: earthquake of magnitude 5.2 at South Sandwich Islands region")
    print("At 04:00:24 on Sun, 01 Oct 2023: earthquake of magnitude 5.3 at 16 km W of Sukabumi, Indonesia")
    print('\t')

if __name__ == "__main__": 
    main()
#! parameters:  starting date (str), ending date (str), minimum earthquake magnitude (float)
#! create a dictionary to store the parameter values necessary for the requests call to USGS
#! use requests.get to fetch a JSON of all earthquakes of at least the given magnitude between the dates