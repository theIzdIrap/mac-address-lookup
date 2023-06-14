#!/usr/bin/python
import json
import requests


o = input("mac : ")
r = requests.get("https://api.macaddress.io/v1?apiKey=<api>&output=json&search=" + o)
lklk = json.loads(r.text)
print("oui " + lklk["vendorDetails"]["oui"])
print("companyName " + lklk["vendorDetails"]["companyName"])
print("companyAddress " + lklk["vendorDetails"]["companyAddress"])
print("countryCode " + lklk["vendorDetails"]["countryCode"])
print("borderLeft " + lklk["blockDetails"]["borderLeft"])
print("borderRight " + lklk["blockDetails"]["borderRight"])
print("assignmentBlockSize " + lklk["blockDetails"]["assignmentBlockSize"])
print("dateCreated " + lklk["blockDetails"]["dateCreated"])
print("dateUpdated " + lklk["blockDetails"]["dateUpdated"])
print("searchTerm " + lklk["macAddressDetails"]["searchTerm"])
print("virtualMachine " + lklk["macAddressDetails"]["virtualMachine"])
print("transmissionType " + lklk["macAddressDetails"]["transmissionType"])
print("administrationType " + lklk["macAddressDetails"]["administrationType"])
print("wiresharkNotes " + lklk["macAddressDetails"]["wiresharkNotes"])
print("comment " + lklk["macAddressDetails"]["comment"])
