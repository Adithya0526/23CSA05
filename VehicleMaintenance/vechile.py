from .. import log
from flask import jsonify
import requests

depotURL = r"http://4.224.186.213/evaluation-service/depots"
vechileURL = r"http://4.224.186.213/evaluation-service/vehicles"
depots=requests.get(depotURL).json()
log.Log("backend","info","handler","Depots fetched successfully")
vehicles=requests.get(vechileURL).json()
log.Log("backend","info","handler","Vehicles fetched successfully")
