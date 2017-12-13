import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel 


class Employee(DjangoCassandraModel):
    employee_id = columns.UUID(primary_key=True, default=uuid.uuid4())
    employee_name = columns.Text(max_length=50)
    email = columns.Text(max_length=100)
    password = columns.Text(max_length=10)
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __unicode__(self):
        return '%d %s %s %s' % (self.employee_id,self.employee_name,self.email,self.password)




