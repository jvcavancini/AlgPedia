from algorithm.models import Algorithm
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    help = u"""csv joao carlos"""

    def handle(self, *args, **options):
        try:
            with open('subway_stations.csv', 'w') as csvfile:
                #writer = csv.DictWriter(csvfile, fieldnames=prob_actions)
                users_action = get_users_by_actions()
                for action in users_action.items():
                    print action
                    #csvfile.write(action)
        except:
            import traceback
            traceback.print_exc()
            raise
