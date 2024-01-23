from entities.customer import Customer
from services.customer_service import start, insert, select, update, delete

start()

insert(Customer(None, "Maria", "maria@example.com", "+55(11)98765-4321"))
insert(Customer(None, "John", "john@example.com", "+55(11)12345-6789"))
insert(Customer(None, "Yato", "yato@example.com", "+55(51)90000-0000"))

update(1, Customer(None, "Maria", "maria@example.com", "+55(68)91357-2468"))

print(select(1))

delete(2)