import appsclone_client
import unittest
from appsclone_client.appsCloneClient import *

class TestAppsCloneClient(unittest.TestCase):
  def test_add_id_to_queue(self):
    client = APPSCloneClient("localhost",11,"username","password","dir","dir","queues/idQueueTest")
    client._APPSCloneClient__addIdToQueue(15)

  def test_remove_id_from_queue(self):
    client = APPSCloneClient("localhost",11,"username","password","dir","dir","queues/idQueueTest")
    client._APPSCloneClient__removeIdFromQueue(15)

  def test_get_all_ids_from_queue(self):
    client = APPSCloneClient("localhost",11,"username","password","dir","dir","queues/idQueueTest")
    print(client._APPSCloneClient__getAllIdsFromQueue())

if __name__ == '__main__':
  unittest.main()