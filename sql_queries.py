# DROP TABLES

customers_table_drop = "DROP TABLE IF EXISTS customers;"


# CREATE TABLES
customers_table_create = """CREATE TABLE IF NOT EXISTS customers ( ID varchar, 
                                                                    BALANCE float,
                                                                    BALANCE_FREQUENCY float,
                                                                    PURCHASES float,
                                                                    ONEOFF_PURCHASES float,
                                                                    INSTALLMENTS_PURCHASES float,
                                                                    CASH_ADVANCE float,
                                                                    PURCHASES_FREQUENCY float,
                                                                    ONEOFF_PURCHASES_FREQUENCY float,
                                                                    PURCHASES_INSTALLMENTS_FREQUENCY float,
                                                                    CASH_ADVANCE_FREQUENCY float,
                                                                    CASH_ADVANCE_TRX int,
                                                                    PURCHASES_TRX int,
                                                                    CREDIT_LIMIT float,
                                                                    PAYMENTS float,
                                                                    MINIMUM_PAYMENTS float,
                                                                    PRC_FULL_PAYMENT float,
                                                                    TENURE int
                                                                    );"""

customers_table_insert = ("""INSERT INTO customers(ID ,BALANCE ,BALANCE_FREQUENCY ,PURCHASES ,ONEOFF_PURCHASES ,INSTALLMENTS_PURCHASES ,
CASH_ADVANCE ,PURCHASES_FREQUENCY ,ONEOFF_PURCHASES_FREQUENCY ,PURCHASES_INSTALLMENTS_FREQUENCY ,CASH_ADVANCE_FREQUENCY ,
CASH_ADVANCE_TRX ,PURCHASES_TRX ,CREDIT_LIMIT , PAYMENTS , MINIMUM_PAYMENTS , PRC_FULL_PAYMENT ,TENURE ) 
                            VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)
                            --ON CONFLICT (ID)
                            --DO NOTHING
                            ;""")