from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://inspire.misoportal.com/geoserver/portsmouth_city_council_polling_stations2015_point/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=portsmouth_city_council_polling_stations2015_point"
council_id = 'E06000044'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
