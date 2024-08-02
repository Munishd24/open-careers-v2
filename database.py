from sqlalchemy import create_engine, text


engine = create_engine("mysql+mysqldb://sql12723055:3BIxTsZy15@sql12.freesqldatabase.com/sql12723055",
                       pool_recycle=3600, echo=True)


# database stored in cloud
def load_jobs_from_db():
    
 with engine.connect() as conn:
    result = conn.execute(text("Select * from jobs"))

    jobs = []
    for row in result.all():
        jobs.append(row._mapping)
    return jobs

