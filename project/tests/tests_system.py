import os, sys, logging
import sqlite3
import pandas as pd
from pandas.testing import assert_frame_equal

class TestSystem:
    def test_weather(self, yagon_pipeline, mandalay_pipeline,naypyitaw_pipeline):
        yagon_pipeline.run_pipeline()
        yagon_loader=yagon_pipeline.extractor.file_handlers[0].loader
        db_path = os.path.join(yagon_loader.output_directory, yagon_loader.db_name)
        try:
            connection = sqlite3.connect(db_path)
            result = pd.read_sql_query(f"SELECT * FROM {yagon_loader.table_name}", connection)
        except sqlite3.Error as e:
            logging.error(msg=f"Error while creating SQLite DB: {e}")
            sys.exit(1)
        finally:
            connection.close()
        yagon_transformed_data = yagon_pipeline.extractor.file_handlers[0]._data_frame
        assert_frame_equal(result, yagon_transformed_data)
        
        
        
        mandalay_pipeline.run_pipeline()
        mandalay_loader=mandalay_pipeline.extractor.file_handlers[0].loader
        db_path = os.path.join(mandalay_loader.output_directory, mandalay_loader.db_name)
        try:
            connection = sqlite3.connect(db_path)
            result = pd.read_sql_query(f"SELECT * FROM {mandalay_loader.table_name}", connection)
        except sqlite3.Error as e:
            logging.error(msg=f"Error while creating SQLite DB: {e}")
            sys.exit(1)
        finally:
            connection.close()
        mandalay_transformed_data = mandalay_pipeline.extractor.file_handlers[0]._data_frame
        merged_data=pd.concat([yagon_transformed_data,mandalay_transformed_data], axis=0,ignore_index=True)
        assert_frame_equal(result,merged_data)
        
        
        naypyitaw_pipeline.run_pipeline()
        naypyitaw_loader=naypyitaw_pipeline.extractor.file_handlers[0].loader
        db_path = os.path.join(naypyitaw_loader.output_directory, naypyitaw_loader.db_name)
        try:
            connection = sqlite3.connect(db_path)
            result = pd.read_sql_query(f"SELECT * FROM {naypyitaw_loader.table_name}", connection)
        except sqlite3.Error as e:
            logging.error(msg=f"Error while creating SQLite DB: {e}")
            sys.exit(1)
        finally:
            connection.close()
        naypyitaw_transformed_data = naypyitaw_pipeline.extractor.file_handlers[0]._data_frame
        merged_data=pd.concat([yagon_transformed_data,mandalay_transformed_data,naypyitaw_transformed_data], axis=0,ignore_index=True)
        assert_frame_equal(result,merged_data)
        os.remove(db_path)

        
    def test_supermarket_sales(self,sales_pipeline):
        sales_pipeline.run_pipeline()
        sales_pipeline_loader=sales_pipeline.extractor.file_handlers[0].loader
        db_path = os.path.join(sales_pipeline_loader.output_directory, sales_pipeline_loader.db_name)
        try:
            connection = sqlite3.connect(db_path)
            result = pd.read_sql_query(f"SELECT * FROM {sales_pipeline_loader.table_name}", connection)
        except sqlite3.Error as e:
            logging.error(msg=f"Error while creating SQLite DB: {e}")
            sys.exit(1)
        finally:
            connection.close()
        sales_pipeline_transformed_data = sales_pipeline.extractor.file_handlers[0]._data_frame
        assert_frame_equal(result,sales_pipeline_transformed_data)
        os.remove(db_path)
    