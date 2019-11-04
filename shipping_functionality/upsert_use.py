#import os
#import sys
#import time

#import numpy as np
import pandas as pd
from timeit import default_timer as timer
from sqlalchemy import create_engine
#from upsert import clean_df_db_dups

def setup(engine, tablename):
    engine.execute("""DROP TABLE IF EXISTS "%s" """ % (tablename))
    engine.execute("SELECT ship_name FROM yang_ming_daily_noon").fetchall()

    engine.execute("""CREATE TABLE "%s" (
                  "A" INTEGER,
                  "B" INTEGER,
                  "C" INTEGER,
                  "D" INTEGER,
                  CONSTRAINT pk_A_B PRIMARY KEY ("A","B"))
                  """ % (tablename))

if __name__ == '__main__':
    DB_TYPE = 'mysql'
    DB_DRIVER = 'pymysql'
    DB_USER = 'fm'
    DB_PASS = 'password'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = 'mydb'
    POOL_SIZE = 50
    TABLENAME = 'yang_ming_daily_noon'
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s/%s' % (DB_TYPE,DB_DRIVER,DB_USER,
                                                          DB_PASS, DB_HOST,DB_NAME)
    ENGINE = create_engine(
        SQLALCHEMY_DATABASE_URI)

    print ('setting up db')
    setup(ENGINE, TABLENAME)

    try:


            #print('running test %s' %(str(i)))
            #colmn_name   = pd.read_csv('C:/Users/Abhi/Documents/myDB.csv') #try importing directly from database
            #df = pd.read_excel('C:/Users/Abhi/Downloads/04oct2018to16apr2019.xlsx')
            #colmn1= df.iloc[5:df.shape[0] - 2][0]
            #inserted = pd.read_sql('SELECT count("ship_name") from %s' % (TABLENAME), ENGINE)
            #df.to_sql(TABLENAME, ENGINE, if_exists='append', )
            #extra_data = pd.DataFrame({'ship_name': list(colmn1)})
            df=pd.read_sql_table(TABLENAME,ENGINE)

            #df = pd.DataFrame(
                #np.random.randint(0, 200, size=df.shape), columns=list(colmn_name.columns))
            '''df = clean_df_db_dups(df, TABLENAME, ENGINE, dup_cols=list(colmn_name.columns))
            print('row count after drop db duplicates is now : %s' %(df.shape[0]))
            df.to_sql(TABLENAME, ENGINE, if_exists='append', index=False)
            i += 1
        end = timer()
        elapsed_time = end - start
        print('completed singlethread insert loops in %s sec!' %(elapsed_time))
        inserted = pd.read_sql('SELECT count(*) from %s' %(TABLENAME), ENGINE)
        print('inserted %s new rows into database!' %(inserted.iloc[0]['count']))'''

    except KeyboardInterrupt:
        print("Interrupted... exiting...")