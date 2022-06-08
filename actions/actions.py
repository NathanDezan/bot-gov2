from asyncio.windows_events import NULL
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
from random import randint

uri = "mongodb+srv://dezan:8snD47gyz6VS5b6o@bot-gov2.bheeh.mongodb.net/?retryWrites=true&w=majority"
#senha: 8snD47gyz6VS5b6o

class Action_function(Action):
    def name(self) -> Text:
        return "action_function"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cpf = tracker.get_slot('cpf_slot')
        result = Action_function.check_account(cpf)

        if result != None:
            name = result["name"]
            address = result["informations"]["address"]
            phone = result["phone"]
            number = result["informations"]["number"]
            district = result["informations"]["district"]
            reference = result["informations"]["reference"]

            dispatcher.utter_message(text=f"{name} residente no endereço {address}, {number} - {district} - {reference} de telefone {phone}. As informações estão corretas? (informe \"sim\" ou \"não\")")
        else:
            print("Nao achei o cpf informado")

        return []

    def add_account(name, cpf, phone, address, number, district, reference):
        result = {"cpf": cpf, "name": name, "phone": phone, "informations": {"address": address, "number": number, "district": district, "reference": reference}}

        try:
            client = MongoClient(uri)
            db = client["bot-gov2"]
            collection = db["clients"]
            collection.insert_one(result)
        except:
            print("Error connecting to database.")
    
    def check_account(cpf_insert):
        try:
            client = MongoClient(uri)
            db = client["bot-gov2"]
            collection = db["clients"]
            return collection.find_one({"cpf": cpf_insert})
        except:
            print("Error connecting to database.")
        return NULL

class Action_request(Action):
    def name(self) -> Text:
        return "action_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        burguer = tracker.get_slot('hamburguer_slot')
        burguer = burguer.lower()
        list_prices = [{"x-bacon": "R$15,00", "x-salada": "R$12,00", "x-cheedar": "R$16,00", "x-infarto": "R$19,00"}]
        id_request = randint(10000, 9999999)
        price_burguer = ""

        for i in list_prices[0]:
            if i == burguer:
                price_burguer = list_prices[0][i]

        dispatcher.utter_message(text=f"O ID de seu pedido é {id_request}.\nDetalhes do pedido: {burguer}.\nValor total: {price_burguer}.\nAgradecemos a preferência :).")

        return []