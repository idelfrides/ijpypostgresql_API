"""
#!/usr/bin/python
------------------------------------------------------
   ====  PACKAGE INFORMATION  ====
 App name: ijpypostgresql
 Description: module to handle data from postgreSQL
              DB with python 3.x
 @utor: Engineer Idelfrides Jorge
 Date started: aug. 3rd, 2019
 Date finished: aug. 8th, 2019
 License: on the README.md file
 Email: idelfridesjorgepapai@gmail.com
 GitHub: @idelfrides(https:\\github.com/idelfrides/)
 ------------------------------------------------------
   ====  TECHNICAL INFORMATION  ====
 Python Interpreter:
 --> Python 3.6.2

Python driver for postgreSQL database:
   --> psycopg2 v2.8.3
   -*- Coding: UTF-8 -*-
 content-type: script/python; utf-8
 ------------------------------------------------------
"""

# --------------------------------------------------
# importing my owm modules
# --------------------------------------------------
from ijpypostgresql import HelperModule as hm

# --------------------------------------------------
# importing the python module
# --------------------------------------------------

import psycopg2   # postgresql db driver for python

class ModulePostgreSQLdb(object):
    """
       ---------------------------------------------------
          ====  OPERATIONAL INFORMATION  =====
         This module will be my library for python
         appications working with MysSQL DB.
         The module will create all method needed to
         manage a db app and more other methods.
       ---------------------------------------------------
    """    
    
    # create an o=instance of HelperModule module
    hmo = hm.HelperModule()
    
    
    # ----------------------------------------------
    # set db and all tables name bere to better
    # controle this app.
    # ----------------------------------------------
    appdb = 'test'              # define  db name
    # pg_db = 'postgres'
    tb_test = 'tb_test'
    dev_tb = 'developer'
    person_table = 'person'     # define table name
    car_table = 'car'           # define manager table
    # sup_table = 'supervisor'  # define supervisor table
    
    
    def __init__(self):
        """
           -------------------------------------------------
            The thunder init method inicialize and show
            the module information to user via terminal by
            calling method 'app_info()'
           -------------------------------------------------
           
           :type self: auto reference parameter
           :rtype: None
        """
        self.hmo.app_info()


   
    def connect2db(self):
        """
           ------------------------------------------------------
             This method set connection to the local server,
             with na 'database' created. It need to set a DB.
             This method is only called on your main module,
             the same used to test the 'ijpypostgresql' package.
             retu  'connection' with db and 'cursor'
             to execute quereis
           ------------------------------------------------------
           
           :type self: auto reference parameter
           :rtype: connection with postgre | cursor of that connection
        """
      
        print("\n  I AM A CNONNECTION WITH DB: connect2db \n")

        ''' Connect to the postgreSQL database server '''
        conn = None
        cursor = None
        try:
            # make a connection
            conn = psycopg2.connect(
                host='127.0.0.1',   # 127.0.0.1 | localhost
                port = '5432',
                database='test',
                user='postgres',
                password='pgdbijdev'
            )
            # create a cursor
            cursor = conn.cursor()

            # print PostgresSQL connecion proprieties
            prop = conn.get_dsn_parameters()
            print('\n PostgresSQL connecion proprieties \n {}'.format(prop) )

            # execute a statement; eecute a query; fetch the first
            # version of postgres db version and display the PostgreSQL
            # database server version
            print('\n PostgreSQL database version:\n ')
            cursor.execute('SELECT version()')
            version = cursor.fetchone()
            print('\n You are connected to server \n {}'.format(version))
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error while tring to connect to POSTGRESQL DB: {}. \n Server reponse: {}'.format('test', error))
        finally:
            if conn is not None:
                print('\n Connection setted up successfuly \n')

        return conn, cursor


    
    def create_db(self, cursor, db):
        """
           -------------------------------------------------
             This method create a DB to be used on
             this package. The db is define by you/user as
             an attribute of this module(see on the to).
           -------------------------------------------------
           
           :type cur: cursor of postgreSQL connection
           :type db: data base name to be created
           :rtype: None
        """
        try:
            sql = "CREATE DATABASE " + db
            cursor.execute(sql)
            print("\n Database {} created successfully. \n ".format(db))
        except Exception as erro:
            print('Error by try to CREATE DB: {}. \n Server reponse: {}'.format(self.appdb, erro))


    
    def activate_db(self, cur, db):
        """
           -------------------------------------------------
            This method activate the DB to be used to test
            this package.
           -------------------------------------------------
           
           :type cur: cursor of postgreSQL connection
           :type db: data base name to be created
           :rtype: None
        """
        try:
            sql_use = "USE " + db
            cur.execute(sql_use)
            print('\n Database {} activated successfuly'.format(db))
        except Exception as error:
            print('\n Error try to activate DB {}. \n Server said: {}'.format(db, error))

            
    
    def create_table(self, cur, mytb):
        """
           --------------------------------------------------
            This method create a table to the DB and be
            used on this package. Al tables is defined by
            you/user like  an attribute of this
            module(see on the to).
           --------------------------------------------------
           
           :type cur: cursor of postgreSQL connection
           :type mydb: database name where a table will be created
           :rtype: None
        """
        # cursor_conec = self.set_conec_with_db()
        sql_1 = "CREATE TABLE IF NOT EXISTS " + mytb
        myfields = " (id BIGSERIAL NOT NULL PRIMARY KEY, " \
                   " name VARCHAR(255)," \
                   " gender VARCHAR(50)," \
                   " company VARCHAR(255), " \
                   " age INT, " \
                   " salary NUMERIC(7, 2))"
        sql = sql_1 +  myfields
        try:
            cur.execute(sql)
            print("\n Table {} created successfully. \n ".format(mytb))
        except Exception as erro:
            print('\n Error by try to create the table: {}. \n Server reponse: {}'.format(mytb, erro))

 
    def alter_table(self, cur, mytb, oper, atrib):
        """
           -------------------------------------------------
             This method alter a table present on DB.
             The method provide 3 operations: add, drop
             and modify. The tables and operation are
             defined by you/user like an attribute(tables)
             of this module(see on the to).
           -------------------------------------------------
           
           :type cur: cursor of postgreSQL connection
           :type mydb: database name, witch contain the
                       table that the attibute gonna be altered
           :type oper: the operation to be perform over the attribute atrib
           :type atrib: attibute will be altered
           :rtype: None
        """
        # cur = self.set_conec_with_db()
        if oper is 'add':
            sql_1 = " ALTER TABLE " + mytb
            newattri = " ADD COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + newattri
            print(sql)
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper is 'drop':
            sql_1 = "ALTER TABLE " + mytb
            drop_attri = " DROP COLUMN " + atrib
            sql = sql_1 + drop_attri
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper is 'mod':
            sql_1 = "ALTER TABLE " + mytb
            mod_attri = " MODIFY COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + mod_attri
            try:
                cur.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        else:
            pass

    def drop_struct(self, con, cur, code, entity):
        """        
           --------------------------------------------------
            This method DROP a db/table exists.
            The method has 3 parameters: cursor of conection,
            code of struct and the name(entity) of the same.
           --------------------------------------------------
           
           :type con: connection with postgreSQL DB
           :type cur: cursor of postgreSQL connection
           :type code: code of struct. Can be database (db) or table (tb)
           :type entity: name of the structure defined by code parameter. 
           :rtype: None
        """
         
        # cur = self.set_conec_with_db()
        op = self.hmo.info_danger(code, entity)
        if code is 'db':
            if op == 1:   # drop
                sql = " DROP DATABASE IF EXISTS " + entity
                try:
                    cur.execute(sql)
                    # con.comit()
                    print("\n Database {}  was droped  successfully. \n ".format(entity))
                except Exception as erro:
                    print('\n Error try to DROP the Database: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:   # operation aborted
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
        elif code is 'tb':
            if op == 1:
                # sql = " DROP TABLE IF EXISTS " + entity
                sql = " DROP TABLE " + entity
                try:
                    cur.execute(sql)
                    # con.comit()
                    print("\n Table {} was droped successfully. \n ".format(entity))
                except Exception as erro:
                    print('\n Error try to DROP the table: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
            else:
                pass
        else:
            pass


    def truncate(self, con, cur, mytb):
        """        
           --------------------------------------------------
             This method TRUNCATE a table presents on DB.
             The method has 3 parameters: connection, cursor
             and the table that going to be truncated.
           --------------------------------------------------          
           
           :type con: connection with postgreSQL DB
           :type cur: cursor of postgreSQL connection
           :type mydb: database name, witch contain the
                       table that the attibute gonna be truncated
           :rtype; None
        """
        try:
            sql = " TRUNCATE TABLE " + mytb
            cur.execute(sql)
            # con.comit()
            print("\n Table {} TRUNCATED successfully. \n ".format(mytb))
        except Exception as error:
            print('\n Error by try to TRUNCATE the table: {}. \n Server reponse: {}'.format(mytb, error))


   
    def entity_verify(self, cur, entity):
         """
            -----------------------------------------------------
              This method make a verification of a struct: db
              or table presents on DB.
              The method show(via run terminal) all db existis
              on the localhost or all tables on a specific db.
            ------------------------------------------------------
            
            :type cur: cursor of postgreSQL connection
            :type entity: name of the structure: db or tb. 
            :rtype: None
         """
         
        if entity is 'db':
            print('\n VERIFY DB')
            try:
                cur.execute("SHOW DATABASES")
                for db in cur:
                    print('\n tipo: ', type(db))
                    print(' {}'.format(db))
            except Exception as error:
                print('Error by try to show all DB. \n Server said: {}'.format(error))
        elif entity is 'tb':
            print('\n VERIFY TB')
            try:
                cur.execute("SHOW TABLES")
                for tb in cur:
                    print('\n tipo: ', type(tb))
                    print(' {}'.format(tb))
            except Exception as error:
                print('Error by try to show all tables. \n Server said: {}'.format(error))
        else:
            pass

    
    def unique_constraint(self, cur, attr, table, oper):
        """
           ------------------------------------------------------
             This method alter a table present on DB to make
             an attr as UNIQUE. It provide 2 operations: Add | Drop
             The table, operation and attribute
             are defined by you/user as arguments of method.
           ------------------------------------------------------
           
           :type cur: cursor of postgreSQL connection
           :type attr: attibute to make unique 
           :type table: the table that contain the attribute
           :type oper: the operations to be perform
           :rtype: None
        """
        unique_const_name = table + '_' + attr + '_' + 'key'
        if oper is 'add':
            print('\n ADDING ATTR {} AS UNIQUE IN TABLE {}'.format(attr, table))
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' ADD CONSTRAINT ' + unique_const_name + ' UNIQUE(attr)'
                sql = sql_1 + sql_2
                cur.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to MAKE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        elif oper is 'drop':
            print('\n DROPPING UNIQUE CONSTRAINT FROM ATTR {} IN TABLE {}'.format(attr, table))
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' DROP CONSTRAINT ' + unique_const_name
                sql = sql_1 + sql_2
                cur.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to REMOVE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        else:
            pass


    def close_pg_con(self, con, cur):
        """
           ---------------------------------------------------
             This method close the connection with mySQL
             server. The conn only or cursor only or both them
           ---------------------------------------------------
           
           :type con: connection with postgreSQL DB
           :type cur: cursor of postgreSQL connection
           :rtype: None
        """
        try:
            cur.close()
            con.close()
            print('\n PostgreSQL connection is closed successfuly \n')
        except Exception as error:
            print('Error by tring to CLOSE the connection with PostgreSQL server {}. \n\n Server said: {}'.format(con, error))
       
