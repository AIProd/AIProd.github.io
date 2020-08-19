# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import requests as re
import json
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)
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
class action_greet_user(Action):
#Ask for user number and raise a ticket in his name for a demo
     def name(self) -> Text:
         """Unique identifier of the form"""
         return "action_greet_user"

     def run(self, dispatcher, tracker, domain) -> List[EventType]:
        # if we dont know the product the user is migrating from,
        # store his last message in a slot.
         language = tracker.get_slot("person_name")
         if language is null:
            return [
                SlotSet("person_name", "There"),
            ]

class ActionFormInfo(FormAction):

     def name(self) -> Text:
         """Unique identifier of the form"""
         return "crop_disease_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         """A list of required slots that the form has to fill"""
         return ["crop", "disease"]
		 
     def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
			 #"""Define what the form has to do after all required slots are filled"""
				# utter submit template
         buttons = []
         buttons.append({"title": "Yes", "payload": "Yes"})
         buttons.append({"title": "No", "payload": "No! I would like to correct some information."})
         dispatcher.utter_message(template = 'utter_submit', buttons = buttons)
         return []
	 
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
         """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message or a list of them, where a first match will be picked"""
         return {
            "crop": [self.from_entity(entity="crop"), self.from_text(intent="crop_disease")], 
            "disease": [self.from_entity(entity="disease"), self.from_text(intent="crop_disease")]}

class product_input_form(FormAction):
#A function to map product name to slot and give the relevant information to customer

     def name(self) -> Text:
         """Unique identifier of the form"""
         return "product_input"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         """A list of required slots that the form has to fill"""
         return ["product"]
	 
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
         """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message or a list of them, where a first match will be picked"""
         return {
            "product": [self.from_entity(entity="product"), self.from_text(intent="product_only")], 
            }

class location_input_form(FormAction):
#Map the location of user to region and find out the shops in that area.
     def name(self) -> Text:
         """Unique identifier of the form"""
         return "user_location_input"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         """A list of required slots that the form has to fill"""
         return ["region"]
	 
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
         """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message or a list of them, where a first match will be picked"""
         return {
            "region": [self.from_entity(entity="region"), self.from_text(intent="user_location")], 
            }

class Number_input_form(Action):
#Ask for user number and raise a ticket in his name for a demo
     def name(self) -> Text:
         """Unique identifier of the form"""
         return "action_contact_number_input"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         """A list of required slots that the form has to fill"""
         return ["number"]
	 
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
         """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message or a list of them, where a first match will be picked"""
         return {
            "number": [self.from_entity(entity="number"), self.from_text(intent="demo_only")], 
            }



      