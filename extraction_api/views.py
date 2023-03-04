from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import openai
import fitz
import sys

# Create your views here.
@api_view(['GET'])
def getText(request):
    api_key ="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"
    # if not args:
    #     filename = sys.argv[1]
    # else:
    #     filename = args[0]
    # ofile = filename + ".txt"
    # doc = fitz.open(filename)
    

    # for page in doc:
    #     txt = page.get_text().encode("utf-8") + bytes((12,))
    
    # openai.api_key = api_key
    # start_sequence = "\nA:"
    # restart_sequence = "\n\nQ: "

    # # print("Consider the following text enclosed within double quotes: \"{text}\".This is the resume of a person applying for a job. Please see from the resume if the following conditions are met:\n1. The person has had undergraduate education in CET\n2. The person has done projects in React.\n3. The person has work experience using django.\n4. The person has work experience using tensorflow.\n5. The person has served some sort of leadership roles.\nNow return a json file for the each of the above requirements with key as the question number and value as True or False depending on the query.".format(text=txt))

    # response = openai.Completion.create(
    # model= "text-davinci-003",
    # prompt= "Consider the following text enclosed within double quotes: \"{text}\".This is the resume of a person applying for a job. Please see from the resume if the following conditions are met:\n1. The person has had undergraduate education in CET\n2. The person has done projects in React.\n3. The person has work experience using django.\n4. The person has work experience using tensorflow.\n5. The person has served some sort of leadership roles.\nNow return a json file for the each of the above requirements with key as the question number and value as True or False depending on the query.".format(text=txt),
    # max_tokens= 1000,
    # temperature= 0,
    # top_p= 1,
    # n= 1,
    # stream= False,
    # logprobs= None,
    # stop= "{}"
    # )
    # return Response(type(response))
    return Response("hi")
