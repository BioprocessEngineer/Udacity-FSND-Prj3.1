#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

def tab(c, results):
	widths = [max(len(str(x)) for x in line) for line in zip(*results)]
	columns = []
	tavnit = '|'
	separator = '+' 

	for cd in c.description:
	    columns.append(cd[0])

	for w in widths:
	    tavnit += " %-"+"%ss |" % (w,)
	    separator += '-'*w + '--+'

	print(separator)
	print(tavnit % tuple(columns))
	print(separator)
	for row in results:
	    print(tavnit % row)
	print(separator)

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("""select count(log.path) as Views, articles.title from log, articles 
	where log.status LIKE '%OK%' AND log.path LIKE CONCAT('%', articles.slug, '%') 
	group by articles.title 
	order by Views desc 
	limit 3;""")
results = c.fetchall()
tab(c, results)

c.execute("""select count(log.path) as Views, authors.name from log, articles, authors 
	where log.status LIKE '%OK%' 
	AND log.path LIKE CONCAT('%', articles.slug, '%') 
	AND articles.author=authors.id 
	group by authors.name 
	order by Views desc;""")
results = c.fetchall()
tab(c, results)

c.execute("""select error.num * 100.0/ total.num as error_percentage, total.date 
	from error, total 
	where error.date=total.date 
	AND (error.num * 100.0/ total.num) > 2;""")
results = c.fetchall()
tab(c, results)
db.close()
