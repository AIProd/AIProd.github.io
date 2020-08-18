# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        facility = tracker.get_slot("facility_type")
        address = tracker.get_slot("location")

        address_place=""
        if(address.lower() == "indirapuram"):
            address_place = "GC Grand Tower, Shop no-2 ground, street market, Vaibhav Khand, Indirapuram, Ghaziabad, Uttar Pradesh 201010"
        elif(address.lower() == "balewadi"):
            address_place = "My World Society, Balewadi High Street Road, Baner, Pune"

        dispatcher.utter_message(text="Here is the address {}:{}".format(facility, address_place))

        return [SlotSet("address", address_place)]

