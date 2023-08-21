# Web Scraping H&M T-Shirts Data

This project uses Scrapy, a Python web scraping framework, to extract information about men's t-shirts from the H&M website. The scraped data is saved using the HmTshirtsItem item class.

## Project Structure

- **spiders/hm.py**: Contains the Spider class for crawling the H&M t-shirts pages and extracting data.
- **items.py**: Defines the HmTshirtsItem class to structure the scraped data.
- **settings.py**: Configuration settings for the Scrapy project.
- **pipelines.py**: Contains the pipeline to process and save the scraped data.

## How to Run

1. Install Scrapy if not already installed:
   ```bash
   pip install scrapy
2. Navigate to the project folder containing scrapy.cfg.
3. To start crawling, run the following command:
   ```bash
   scrapy crawl hm
4. The scraped data will be saved in the output file defined in pipelines.py.

## Spider python file
hm_tshirts > hm_tshirts > spiders > hm.py

## CSV Data file
hm_tshirts > hm.csv

# Output Data
## Scaped Data

The scraped data includes the following information about each t-shirt:

- Name
- Color
- Description
- SKU
- Brand
- Price
- Availability

## Note

- Make sure to respect the website's `robots.txt` file and terms of use while scraping.
- Be mindful of web scraping ethics and legality.

## Contact

For any questions or feedback, feel free to contact.
---
By 
Daksh Sethi  
email- thedakshsethi@gmail.com
