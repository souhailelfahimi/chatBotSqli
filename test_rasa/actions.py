# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import json


import requests
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from test import search
class ActionAskType(Action):
	def name(self):
		return 'action_ask_type'


	def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		confidence=tracker.latest_message['intent'].get('confidence')
		print("confidence", confidence)
		print("intent", tracker.latest_message['intent'].get('name'))
		if confidence<0.85:
			list = search(tracker.latest_message.get('text'))
			response = ""
			for i in list:
				response += i + "\n"
		else:
			response = """whish type?""".format(
			)

		dispatcher.utter_message(response)
		return []
class ActionAskGPE(Action):
	def name(self):
		return 'action_ask_GPE'

	def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		confidence=tracker.latest_message['intent'].get('confidence')
		print("confidence", confidence)
		print("intent", tracker.latest_message['intent'].get('name'))
		if confidence<0.85:
			list = search(tracker.latest_message.get('text'))
			response = ""
			for i in list:
				response += i + "\n"
		else:
			response = """In what location?""".format()

		dispatcher.utter_message(response)
		return []
class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		loc = tracker.get_slot('GPE')


		response = """It is currently   in {} at the moment.""".format(
			loc)

		dispatcher.utter_message(response)
		return []

class ActionCard(Action):
		def name(self):
			return 'action_card'
		def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
			entities={}

			loc = tracker.get_slot('GPE')
			type = tracker.get_slot('type_card')
			entities["GPE"]=loc
			entities["type_card"] = type
			intent="getCard"
			print(intent)
			print(loc)
			print(type)
			headers = {'Content-type': 'application/json;charset=UTF-8'}
			data = dict(name=intent,predefinedEntities=[dict(name=loc),dict(name=type)])

			print()
			r = requests.post(url='http://localhost:8080/domains', data=json.dumps(data), headers=headers)

			print(r.text)

			response = """{}""".format(r.text
				)


			dispatcher.utter_message(response)
			return []


class ActionHealtCheck(Action):

    def name(self) -> Text:
        return "action_healt_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        service_name = tracker.get_slot('service_name')
        env_name = tracker.get_slot('env_name')
        if(env_name == ""):
            env_name = "vst"

        response = """ service_name {} env_name {}""".format(
            service_name, env_name)

        dispatcher.utter_message(response)

        return []

class ActionStackOverFlow(Action):
			"""This action class allows to display buttons for each facility type
            for the user to chose from to fill the facility_type entity slot."""

			def name(self) -> Text:
				"""Unique identifier of the action"""

				return "search_stackoverflow"

			def run(self, dispatcher: CollectingDispatcher,
					tracker: Tracker,
					domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
				list = search(tracker.latest_message.get('text'))
				res = ""
				for i in list:
					res += i + "\n"
				dispatcher.utter_message(text=res)
				return []


