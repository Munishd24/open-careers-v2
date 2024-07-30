from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://sql12723055:3BIxTsZy15@sql12.freesqldatabase.com/sql12723055",
                       pool_recycle=3600, echo=True)

