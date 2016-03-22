## this part of code pulls out all accepted ids from user's account 
from bs4 import BeautifulSoup
import urllib
import os
problem_id = []
no_name = []
contest_id = []
handle = raw_input("Type your handle")

for i in range(1,8):
	print 'grabbing data'
	gen_url = 'http://codeforces.com/submissions/'+handle+'/page/' + str(i)
	r = urllib.urlopen(gen_url)
	print 'done'

	soup = BeautifulSoup(r)
	co = soup.find_all('td')

	for row in range(1,len(co)):
		if len(co[row].attrs) == 4:
			if len(co[row].span.attrs) == 5:
				if co[row].span.attrs['submissionverdict'] == 'OK':
					problem_id.append(co[row].span.attrs['submissionid'])
					no_name.append(row)

	
	for j in range(0,len(no_name)):
		query = no_name[j]
		contest_id.append(co[query-2].a.attrs['href'].split('/')[3])
	for j in range(0, len(contest_id)):
		url = 'http://codeforces.com/contest/'+contest_id[j]+'/submission/'+problem_id[j]
		strng = contest_id[j]+"-"+problem_id[j]


		target = open(strng, "w")

		print 'getting code '+str(j)+' of page '+str(i)
		r = urllib.urlopen(url)
		print 'got code '+str(j)+' of page '+str(i)
		soup = BeautifulSoup(r)
		co = soup.find_all('div')


		for row in co[26].find_all('pre',attrs={"class" : "program-source"}):
			target.write(row.text)
		target.close()
