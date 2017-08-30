#!/usr/bin/env python2

import psycopg2

DBNAME = "news"


def exec_query(query):
    """Helper function that connects to database and executes queries
    received as arguments"""
    db_connect = psycopg2.connect(database=DBNAME)
    cursr = db_connect.cursor()
    cursr.execute(query)
    results = cursr.fetchall()
    db_connect.close()
    return results


def get_popular_articles():
    """Function that gets and print the three top viewed article
    from the database"""
    articles = exec_query("""SELECT title, num_of_views FROM popu_articles
                          ORDER BY num_of_views DESC LIMIT 3""")
    print("\nMost popular three articles of all the time: ")
    print("_________________________________________________________________")
    for article_title, num_of_views in articles:
        print("\"%s\" - %s views" % (article_title, num_of_views))


def get_popular_author():
    """Function that gets and prints the most popular authors
    from the database"""
    pop_authors = exec_query("""SELECT authors.name, popu_authors.num_of_views
                              FROM popu_authors JOIN authors ON authors.id
                              = popu_authors.author ORDER BY
                              popu_authors.num_of_views DESC""")
    print("\n\nMost Popular article authors of all the time: ")
    print("_________________________________________________________________")
    for author_name, num_of_views in pop_authors:
        print("%s - %s views" % (author_name, num_of_views))


def get_error_percentage():
    """Function that gets and prints days on which more than 1% of requests
    lead to error"""

    rows = exec_query("""SELECT day, error_perc FROM day_with_error_perc
                        WHERE error_perc > 1""")
    print("\n\nDays on which more than 1% of requests lead to error: ")
    print("_________________________________________________________________")
    for date, percent_err in rows:
        print(" {0:%B %d, %Y} - {1:.2f}% errors".format(date, percent_err))
    print("\n")


if __name__ == "__main__":
    print("\n\nLoading results...\n")
    get_popular_articles()
    get_popular_author()
    get_error_percentage()
