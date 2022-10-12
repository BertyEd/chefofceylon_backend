import datetime
from sqlalchemy import Column,Integer, DateTime 


class TimestampMixin(object):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime,default=datetime.datetime.utcnow,nullable=False)
    created_by = Column(Integer,nullable=False)
    modified_at = Column(DateTime,nullable=True)
    modified_by = Column(Integer,nullable=True)
    record_status =  Column(Integer,default=1,nullable=False)