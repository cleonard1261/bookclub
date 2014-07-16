#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Extract data from xml files
#
# Author:   Chad Leonard <cl1008@georgetown.edu>
# Created:  Wed Jul 16 11:26:32 2014 -0400
#
# Copyright (C) 2014
# For license information, see LICENSE.txt
#
# ID: wrangletest.py [] cl1008@georgetown.edu $

"""
Extract data from xml files downloaded
"""

##########################################################################
## Imports
##########################################################################

import unicodedata
import codecs
from lxml import objectify, etree
import psycopg2


##########################################################################
## Database Object
##########################################################################

class Database:
	host = 'localhost'
	user = 'chadleonard'
	passwd = ''
	db = 'bookclub'

	def __init__(self):
		conn = psycopg2.connect(host = self.host,
			                    user = self.user,
			                    password = self.passwd,
			                    dbname = self.db)

		self.cur = conn.cursor()
		conn.autocommit = True


	def query(self, q, p):
		print q 
	 	self.cur.execute(q , p)
	 	#print cur.query
	 	#return self.cur.fetchone()

	def idExists(self, q):
		self.cur.execute(q)
		res = self.cur.fetchone()
		if res[0] > 0:
			return True
		else:
			return False

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
	db = Database()

	path = '../fixtures/8398291-002.xml'
	parsed = objectify.parse(open(path))
	root = parsed.iter()

	for i in root:
		# Parse the Review tags...
		if i.tag == 'review':
			review_id = i.id.text
			rating = i.rating.text
			votes = i.votes.text
			started_at = i.started_at.text
			read_at = i.read_at.text

		# Parse the Book tags...
		if i.tag == 'book':
			book_id = i.id.text
			book_title = i.title.text
			if  i.description.text == None:
				book_desc =  None
			else:
				book_desc = str(i.description.text.encode('utf-8'))
			if  i.num_pages.text == None:
				num_pages =  None
			else:
				num_pages = str(i.num_pages)
			if  i.published.text == None:
				published =  None
			else:
				published = str(i.published.text)

		# Parse the Author tags...
		if i.tag == 'author':
			author_id = i.id.text
			author_name = i.name.text
			image_url = i.image_url.text
			small_image_url = i.small_image_url.text
			link = i.link.text
			average_rating = i.average_rating.text
			ratings_count = i.ratings_count.text
			text_reviews_count = i.text_reviews_count.text

			# Load the Books Table
			q = "select count(*) from bookclub.books where book_id = " +str(book_id)
			if not db.idExists(q):
				db.query("""insert into bookclub.books (book_id, book_title, book_desc, num_pages) values (%s, %s, %s, %s);""", (str(book_id), str(book_title.encode('utf-8')), book_desc, num_pages,))

			# Load the Reviews Table
			q = "select count(*) from bookclub.reviews where review_id = " +str(review_id)
			if not db.idExists(q):
			 	db.query("""insert into bookclub.reviews (review_id, book_id, rating, votes, started_at, read_at) values (%s, %s, %s, %s, %s, %s);""", (str(review_id), str(book_id), str(rating), str(votes), str(started_at), str(read_at),))

			# Load the Authors Table
			q = "select count(*) from bookclub.authors where author_id = " +str(author_id)
			if not db.idExists(q):
				db.query("""insert into bookclub.authors (author_id, author_name, image_url, small_image_url, link, average_rating, ratings_count, text_reviews_count ) values (%s, %s, %s, %s, %s, %s, %s, %s);""", (str(author_id), str(author_name.encode('utf-8')), image_url, small_image_url,link, average_rating, ratings_count, text_reviews_count, ))

			# Load the Books and Authors Relationship Table
			q = "select count(*) from bookclub.books_authors_rltn where author_id = " +str(author_id) +" and book_id = " +str(book_id)
			if not db.idExists(q):
				db.query("""insert into bookclub.books_authors_rltn (author_id, book_id, published) values (%s, %s, %s);""", (str(author_id), str(book_id),  published, ))





