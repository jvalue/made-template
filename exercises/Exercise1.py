import pandas as pd
from sqlalchemy import Column, Integer, String, Float, MetaData, TEXT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create engine & Base 
engine = create_engine("sqlite:///airports.sqlite", echo=True)
Base  = declarative_base()

# Meta data to define the table attributes
meta = MetaData()

# Create Airport class
class Airport(Base):

    # Define table name and columns
    __tablename__ = 'airports'
    column_1 = Column(Integer, primary_key=True)
    column_2 = Column(String(250))
    column_3 = Column(String(250))
    column_4 = Column(String(250))
    column_5 = Column(String(250))
    column_6 = Column(String(250))
    column_7 = Column(Float)
    column_8 = Column(Float)
    column_9 = Column(Float)
    column_10 = Column(Float)
    column_11 = Column(String(1))
    column_12 = Column(TEXT)
    geo_punkt = Column(String(250))

    def __repr__(self) -> str:
        return  '''
                <Airport(column_1='{0}', column_2='{1}', column_3='{2}'
                         column_4='{3}', column_5='{4}', column_6='{5}',
                         column_7='{6}', column_8='{7}', column_9='{8}'
                         column_10='{9}', column_11='{10}', column_12='{11}'
                         geo_punkt='{12}')>'''.format(self.column_1, self.column_2,
                                                     self.column_3, self.column_4,
                                                     self.column_5, self.column_6,
                                                     self.column_6, self.column_8,
                                                     self.column_9, self.column_10,
                                                     self.column_11, self.column_12,
                                                     self.geo_punkt)

meta.create_all(engine)


# Load the dataset
filename = r"rhein-kreis-neuss-flughafen-weltweit.csv"
df = pd.read_csv(filename, delimiter=";")

# Convert the dataframe to sql table
df.to_sql(con=engine, name=Airport.__tablename__, if_exists="replace", index=False)

# Open a session to test the connection
session = sessionmaker()
session.configure(bind=engine)
s = session()

# Desplay the result to the console
results = s.query(Airport).limit(10).all()

print("The first ten rows of the database: ")
for r in results:
    print(r)