
from sqlalchemy import Unicode, Date, Integer, Table, Text, String
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.types

from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, OneToMany, ManyToOne
import camelot.types

class Books( Entity ):

    __tablename__ = 'books'

    title = Column( Unicode(60), nullable = False )
    isbn = Column( Integer(13) )
    pages = Column( Integer(4) )
    first_release_date = Column( Date() )
    genre = Column( Unicode(15) )
    cover = Column( camelot.types.Image( upload_to = 'covers' ) )

    author = ManyToMany( 'Author', tablename = 'books_author', local_colname = 'author_id', remote_colname = 'books_id' )
    translator = ManyToOne( 'Author', backref = 'translated_books' )
        
    publisher = ManyToOne( 'Publisher', required = True, backref = 'books' )

    class Admin( EntityAdmin ):
        from books_summary import BooksSummary
        verbose_name = 'Book'
        list_display = ['title', 
                        'isbn',
                        'pages',
                        'first_release_date',
                        'genre',
                        'cover',
                        'author',
                        'translator',
                        'publisher']

        form_display = ['title',
                        'isbn',
                        'pages',
                        'first_release_date',
                        'genre',
                        'cover',
                        'author',
                        'translator',
                        'publisher']

        form_actions = [
                BooksSummary()
                ]

    def __unicode__( self ):
        return self.title or 'untitled book'
    
class Author( Entity ):
    
    __tablename__ = 'author'
    
    lastname = Column( String(60) )
    firstname = Column( String(60) )
    fullname = column_property(firstname + " " + lastname)
    birthdate = Column( Date() )
    birthlocation = Column( Unicode(40) )
    deathdate = Column( Date() )
    deathlocation = Column( Unicode(40) )
    biographyurl = Column( String(200) )

    books = ManyToMany( 'Books', tablename = 'books_author', local_colname = 'books_id', remote_colname = 'author_id' )
    translated_books = OneToMany( 'Books' )

    class Admin( EntityAdmin ):
        verbose_name = 'Author'
        list_display = [ 'lastname',
                         'firstname',
                         'birthdate',
                         'birthlocation',
                         'deathdate',
                         'deathlocation',
                         'biographyurl' ]
        form_display = list_display + ['books']

    def __unicode__(self):
        return self.fullname or 'unknown author'

class Publisher( Entity ):

    __tablename__ = 'publisher'

    name = Column( Unicode(60) )
    labelname = Column( Unicode(60) )
    countrycode = Column( String(2) )
    location = Column( Unicode(60) )

    books = OneToMany( 'Books' ) 

    class Admin( EntityAdmin ):
        verbose_name = 'Publisher'
        list_display = [ 'name',
                         'labelname',
                         'countrycode',
                         'location' ]

        form_display = list_display + ['publisher']

        def __unicode__( self ):
            return self.name or 'unknown publisher'
