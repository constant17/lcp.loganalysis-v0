
#  Log Analysis Program

The program answers the following questions: 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? and 
3.  On which days did more than 1% of requests lead to errors?
You can launch the program to get the result of the analysis proceeding as follow:

To launch the program,

1. Make sure that you have python installed on your computer
2. Make sure that you have psycopg2 library installed
3. Download the file newsdata.sql from  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
   and load the data into the database news, using the command: `psql -d news -f newsdata.sql`
4. Connect to the database news using the following command: `psql news`
5. Then, create the Views below (`popu_articles`, `popu_authors`, `err_ocurence`, `days`, `day_with_error_perc`)
   by typing the provided syntaxes  Note that if these views are not created the program would not run. 
6. Open the file log_analysis.py with IDLE (Right-click
   on the file and choose "Open with IDLE")
   and Click on "Run" from the menu bar in the IDLE then choose "Run Module" option.
7. Or if you have git bash terminal and a virtual machine on your computer, 
   make sure that your are in the program's directory and launch it from the
   terminal by typing `python log_analysis.py` 
8. The program should launch and display the results obtained from the code.

Create Views in the database `news` using the following syntaxes:

1. popu_articles(title text, num_of_views integer)
	syntax : 
	`CREATE VIEW popu_articles AS SELECT 
    articles.title, COUNT(log.path) AS num_of_views 
    FROM articles JOIN log ON log.path = CONCAT('/article/',  
    articles.slug) WHERE log.status = '200 OK' GROUP BY articles.title`
2. popu_authors(author integer, num_of_views integer)
	syntax :
	`CREATE VIEW popu_authors AS (SELECT 
    articles.author, COUNT(log.path) AS num_of_views 
    FROM articles JOIN log ON log.path = CONCAT('/article/', 
    articles.slug) WHERE log.status = '200 OK' GROUP BY articles.author)`
3. err_ocurence(date date, num_err integer)
	syntax:
	`CREATE VIEW err_occurence AS (SELECT date(time) AS date,
    count(date(time)) AS num_err FROM log WHERE
    status != '200 OK' GROUP BY date)`
4. days(day text, day_num integer)
	syntax:
	`CREATE VIEW days AS (SELECT date(time) AS day,
    COUNT(date(time)) AS day_num FROM log GROUP BY day`
5-  day_with_error_perc(day text, error_perc decimal))
	syntax:
	`CREATE VIEW day_with_error_perc AS (SELECT day, 
    (num_err/day_num::float)*100.0 as error_perc FROM days
    JOIN err_occurence ON (err_occurence.date = days.day))`

Enjoy analyzing logs data!
