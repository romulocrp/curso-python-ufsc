name, fixed, sales = [x for x in input("Insira nome, salário fixo e total de vendas separados por vírgula espaço: ").split(", ")]

total_salary = (0.15 * float(sales)) + float(fixed)

print(f"Nome: {name}, salário fixo: {fixed}, salário total: {total_salary}")