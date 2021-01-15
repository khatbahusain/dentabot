from typing import Dict, Text, Any, List, Union, Optional
import logging
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher



class ActionAppointmentsAvailable(Action):

    def name(self) -> Text:
        return "action_appointments_available"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="rendez-vous : vendredi 12/02/2021 à 10h00")
        return []

class ActionHumanHandoff(Action):

    def name(self) -> Text:
        return "action_human_handoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tmp = 5

        dispatcher.utter_message(text="Un Human arrive dans {} mins".format(tmp))
        return []