import json
import os
import logging
from dotenv import load_dotenv
from datetime import datetime

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# from rasa_sdk.events import SlotSet


load_dotenv(os.path.join(os.getcwd(), ".env"))
logger = logging.getLogger(__name__)


class ActionGetHigh(Action):
    def name(self) -> Text:
        return "action_get_high"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        data_path = os.getenv("BONG_DATA_PATH")

        # Load data file
        with open(data_path, "r") as f:
            data = json.load(f)

        today = datetime.today().strftime("%d-%m-%Y")
        if today in data:
            data[today] += 1
            msg = f"Nouvelle douille ajoutée, ça fait {data[today]} aujourd'hui."
        else:
            data[today] = 1
            msg = "La première douille du jour à été ajoutée."

        # write file
        with open(data_path, "w") as f:
            json.dump(data, f, indent=4)

        dispatcher.utter_message(text=msg)
        logger.info("The data file has been updated")
        return []


class ActionCountBongs(Action):
    def name(self) -> Text:
        return "action_count_bongs"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        data_path = os.getenv("BONG_DATA_PATH")

        # Load data file
        with open(data_path, "r") as f:
            data = json.load(f)

        today = datetime.today().strftime("%d-%m-%Y")

        n_bongs = data.get(today, 0)
        if n_bongs == 0:
            msg = "Aucune douille n'a été fumée aujourd'hui."
        elif n_bongs == 1:
            msg = f"{n_bongs} douille fumée aujourd'hui."
        else:
            msg = f"{n_bongs} douilles fumées aujourd'hui."
        dispatcher.utter_message(text=msg)
        logger.info("✅ The data file has been updated.")
        return []
