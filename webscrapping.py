from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Edge()
driver.get("https://money.rediff.com/gainers")

# getting headers
headers = driver.find_elements(By.XPATH, "//th[normalize-space()='Company']/parent::tr/child::th")
csv_headers = [header.text for header in headers]

# getting table body
rows = driver.find_elements(By.XPATH, "//th[normalize-space()='Company']/ancestor::table/child::tbody/descendant::tr")
rows_data = []

print("Data Writing Started ...")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    cols = [col.text for col in cols]
    rows_data.append(cols)

# saving on file
with open('Parsed.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    writer.writerows(rows_data)

print("Data Writing Finished and saved as Parsed.csv")
driver.close()
