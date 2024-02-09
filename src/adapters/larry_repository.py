import psycopg_pool
import psycopg 
from decimal import Decimal 
from src.adapters.abstract_repository import AbstractRepository
import src.adapters.config as config 
import src.flask_app.database.db_pool as db_pool 


class LarryRepository(AbstractRepository):

    def add(self, line_item):
        print("in repo add")

        qry4 = """
        INSERT INTO line_item (transaction_date, description, account_id, amount, check_number)  
            VALUES (now(), %(description)s, %(account_id)s, %(amount)s, %(check_number)s);
        """
        
        amount = Decimal('20.32')
        check_number = '9787'

        params_both = {
            'description': "Larry larry larry",
            'account_id': 170,
            'amount': amount,
            'check_number': check_number 
            
        }



        # query = """
        # INSERT INTO line_item (
        #     transaction_date,
        #     post_date,
        #     description,
        #     amount,
        #     category_id,
        #     transaction_type_id,
        #     account_id
        # )  
        # VALUES (%s, %s, %s, %s, %s, %s, %s)          
        # """
        # values = (
        #     line_item.transaction_date, 
        #     line_item.post_date,   
        #     line_item.description,           
        #     line_item.amount, 
        #     line_item.category_id, 
        #     line_item.transaction_type_id,
        #     line_item.account_id
        # ) 

        
       

        # results = db_pool.insert(query, values)
        # return results 
        print("in pool default")

        pool_default = psycopg_pool.ConnectionPool(config.DATABASE_STRING,
                                            min_size=config.POOL_MIN_SIZE,
                                            max_size=config.POOL_MAX_SIZE,
                                            max_idle=config.POOL_MAX_IDLE)     

        sel_pool = pool_default

        with sel_pool.connection() as conn:
            cur = conn.cursor(row_factory=psycopg.rows.dict_row)

            cur.execute(qry4, params_both)
            conn.commit()


    def get(self):
        query = """
        SELECT * FROM line_item
        """
        params = {}
        data = db_pool.get_data(query, params, single_row=False)
        return data 
