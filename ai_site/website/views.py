import pickle
import re
import nltk
import json
from nltk.corpus import stopwords
from datetime import datetime   
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def index(response):
    dict = {"westvlaanderen":1,"oostvlaanderen":2,"antwerpen":3,"limburg":4,"vlaamsbrabant":5,"brussel":6,"hennegouwen":7,"waalsbrabant":8,
    "liege":9,"namen":10,"luxemburg":11}
    return render(response,"main/base.html",dict)



