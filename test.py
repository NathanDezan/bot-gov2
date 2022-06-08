# from pymongo import MongoClient

# uri = "mongodb+srv://dezan:8snD47gyz6VS5b6o@bot-gov2.bheeh.mongodb.net/?retryWrites=true&w=majority"

# def check_account(cpf_insert):
#     try:
#         client = MongoClient(uri)
#         db = client["bot-gov2"]
#         collection = db["clients"]
#         return collection.find_one({"cpf": cpf_insert})
#     except:
#         print("Error connecting to database.")

# result = check_account("123.456.789-10")
# print(check_account("123.456.789-10")["name"])

burguer = "X-Bacon"

burguer = burguer.lower()
list_prices = [{"x-bacon": "R$15,00", "x-salada": "R$12,00", "x-cheedar": "R$16,00", "x-infarto": "R$19,00"}]

for i in list_prices[0]:
    print(i)
    print(list_prices[0][i])