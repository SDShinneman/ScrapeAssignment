import urllib2, csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
output = open('electionoutput.csv', 'w')
writer = csv.writer(output)

# Get the html of the page
br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

# Fill out the form
br.select_form(nr = 0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003143']
br.form['ctl00$MainContent$cboRaces'] = ['460006719']

# Submit the form
br.submit('ctl00$MainContent$btnCountyChange')

# Get html
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#Find the main table
main_table = soup.find('table',
	{'id': 'MainContent_dgrdCountyRaceResults'})

#Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)
