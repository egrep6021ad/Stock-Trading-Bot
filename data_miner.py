from pprint import pprint
import os
from datetime import date
import time
from get_history import *
from get_quotes import *
from get_fundamentals import *
from get_options import *
from get_movers import *


today = date.today()
today = str(today)

path = f"./{today}"
exist = os.path.exists(path)
if not exist:
  os.makedirs(path)

my_secret = os.environ['POOP']
poop = my_secret

if __name__ == "__main__":
  try:
    # Returns array of SYMBOLS for days biggest movers:
    arr = getMovers(poop)
    pprint(arr)
    arr = ['NFLX']
    time.sleep(10)
    print("40 Seconds.")
    # Get Quotes for all of those big movers:
    getQuotes(arr,poop)
    time.sleep(10)
    print("30 Seconds..")
    #Get fundamentals on the biggest moverst
    getFundamentals(arr,poop)
    time.sleep(20)
    print("20 Seconds...")
    # Get 3 month breakout on those movers (trend finding / hopping)
    getHistory(arr,poop)
    #Get Options:
    getOptions('TSLA',poop)
  except KeyError:
    print("Key Error!")
  print("DONE")
 

