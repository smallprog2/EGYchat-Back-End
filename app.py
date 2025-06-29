#تثبيت المكاتب و الشبكات العصبية
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
import random
import random
import re
import operator
from transformers import pipeline
import requests
import os
from datetime import datetime
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import scrolledtext
from flask import Flask, request, jsonify


# 1. إعداد بيانات التدريب
# مجموعة الجمل الخاصة بالتحيات

greetings = [
    "hello", "hi", "hey", "good morning", "good evening", "what's up", "how are you", "how's it going",
    "nice to meet you", "greetings", "yo", "hey there", "howdy", "how are you doing", "what's new", 
    "hi there", "how have you been?", "long time no see", "good to see you", "glad to meet you",
    "how are things?", "how’s everything?", "how’s life?", "it’s nice to see you again", "welcome!",
    "hello friend", "how do you do?", "hi buddy", "morning!", "evening!", "hiya!", "sup?", "yo yo!",
    "how’s your day?", ",""what’s good?", "hey", "hi", "good day", "pleased to meet you",
    "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", 
    "Good to see you", "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", 
    "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", 
    "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", 
    "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", 
    "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", 
    "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", 
    "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", 
    "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", 
    "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", "How have you been?", 
    "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", 
    "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", 
    "How’s it going?", "Good to see you", "Long time no see", "How have you been?", "Hello", "Hi", "Hey", 
    "Good morning", "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", 
    "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", 
    "Good to see you", "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", 
    "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", 
    "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", 
    "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", 
    "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", 
    "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", 
    "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", 
    "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", 
    "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", "How have you been?", 
    "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", 
    "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", 
    "How’s it going?", "Good to see you", "Long time no see", "How have you been?", "Hello", "Hi", "Hey", 
    "Good morning", "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", 
    "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", 
    "Good to see you", "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", 
    "Good afternoon", "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", 
    "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", 
    "Long time no see", "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", 
    "Good evening", "What's up?", "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", 
    "Nice to meet you", "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", 
    "How have you been?", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", 
    "Howdy", "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", 
    "Pleased to meet you", "How’s it going?", "Good to see you", "Long time no see", "How have you been?", 
    "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "What's up?", "Howdy", 
    "Greetings", "Yo", "Hi there", "Heya", "Hello there", "Welcome", "Nice to meet you", "Pleased to meet you", 
    "How’s it going?", "Good to see you", "Long time no see", "How have you been?"
]


questions =  [
    "how are you?", "what's your name?", "how old are you?", "what do you do?", "can you help me?",
    "who made you?", "what is the weather like?", "when do you open?", "where are you from?", 
    "do you speak english?", "what time is it?", "how does this work?", "what can you do?", 
    "are you a robot?", "do you understand me?", "where is the bathroom?", "what’s going on?", 
    "what’s your favorite food?", "how was your day?", "why are you here?", "is everything okay?", 
    "can I ask you something?", "what’s the plan?", "where did you go?", "what happened?", 
    "what are you doing?", "when is it?"
]

# مجموعة الجمل الخاصة بالوداع
farewells = [
    "bye", "goodbye", "see you", "see you later", "take care", "i have to go", "talk to you later",
    "catch you later", "see ya", "peace", "farewell", "until next time", "i'm leaving", "good night", 
    "i'll be back", "bye bro", "bye man",    "bye", "goodbye", "see you", "see you later", "take care", "i have to go", "talk to you later",
    "catch you later", "see ya", "peace", "farewell", "until next time", "i'm leaving", "good night",
    "i'll be back", "bye bro", "bye man", "have a nice day", "have a great evening", "talk soon",
    "later", "gotta run", "gotta go", "see you around", "cheerio", "bye for now", "see you tomorrow",
    "i’m signing off", "it’s been a pleasure", "later gator", "goodbye friend", "i’ll catch you later",
    "take care of yourself", "peace out", "until we meet again", "see you next time", "i’ll see you soon",'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you', 'Goodbye', 'Bye', 'See you later', 'Take care', 'Catch you later', 'Farewell', 'See ya', 'Later', 'Bye for now', 'Peace out', 'Have a good one', 'See you soon', 'Until next time', 'All the best', 'Take it easy', 'Be well', 'Adios', 'Ciao', 'So long', 'I’ll be seeing you']

# مجموعة الجمل الخاصة بالشكر
thanks = [
    "thank you", "thanks", "thanks a lot", "thank you very much", "i appreciate it", 
    "thanks for your help", "thanks buddy", "many thanks", "thanks so much", "i’m grateful",    "thank you", "thanks", "thanks a lot", "thank you very much", "i appreciate it", "thanks for your help",
    "thanks buddy", "many thanks", "thanks so much", "i’m grateful", "i appreciate your help",
    "thank you kindly", "thanks a million", "appreciate it", "thanks again", "thank you for everything",
    "i’m so thankful", "i can’t thank you enough", "truly grateful", "big thanks", "a big thank you",
    "massive thanks", "thank you a bunch", "cheers!", "shoutout for helping", "you’re awesome, thanks",
    "thank you very kindly", "super grateful", "thank you for the support", "my thanks to you",
    "eternal thanks", "endless gratitude", "a heartfelt thank you",'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful', 'Thank you', 'Thanks', 'Much appreciated', 'Thanks a lot', 'Thank you so much', 'I appreciate it', 'Many thanks', 'Thanks a million', 'Thanks a ton', 'Thank you kindly', 'Sincerely thanks', 'Thanks again', 'Thanks a bunch', 'Grateful for this', 'Big thanks', 'Endless thanks', 'Thank you very much', 'Thanks heaps', 'Thanks for everything', 'Deeply grateful']


# مجموعة الجمل الخاصة بطلب المساعدة
help_requests = [
    "i need help", "can you help me", "help me please", "i need some assistance", "i have a problem",
    "can you assist me", "i dont know what to do", "can you support me", "could you help", "please help","i need help", "can you help me", "help me please", "i need some assistance", "i have a problem",
    "can you assist me", "i don’t know what to do", "can you support me", "could you help", "please help",
    "help would be appreciated", "i need a hand", "could you give me a hand?", "can you guide me?",
    "i’m stuck", "can you explain this?", "need your help urgently", "any chance you could help?",
    "help me out here", "lend me a hand", "i’d appreciate your help", "can you walk me through this?",
    "could you clarify?", "i’m lost, help!", "i need backup", "i can’t do this alone", "please assist",
    "help me understand", "a little help here?", "don’t know what to do", "some guidance please",
    "looking for assistance", "could use your support", "need assistance asap", "help is needed here",
    "need your input", "need clarification", "can you solve this for me?",'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?', 'Can you help me?', 'I need assistance', 'Could you give me a hand?', 'Would you mind helping me?', 'Could you assist me?', 'Can I get some help?', 'Would you help me out?', 'Could you do me a favor?', 'I could use some help', 'May I ask for your help?', 'I need your help', 'Please help me', 'I’m looking for help', 'Do you mind helping?', 'Can you support me?', 'Would you lend a hand?', 'Could you spare a moment to help?', 'I’d appreciate your help', 'Is it okay if you help?', 'Could I get assistance?'

]

# دمج جميع الجمل في قائمة واحدة
texts = greetings + questions + farewells + thanks + help_requests
# تعيين التصنيفات (label) لكل جملة على حسب نوعها
labels = (
    ["greeting"] * len(greetings) +  # جمل التحية
    ["question"] * len(questions) +  # جمل الأسئلة
    ["farewell"] * len(farewells) +  # جمل الوداع
    ["thanks"] * len(thanks) +  # جمل الشكر
    ["help"] * len(help_requests)  # جمل طلب المساعدة
)
# 3. تحويل النصوص إلى أرقام باستخدام CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()  # تحويل الجمل إلى مصفوفة أرقام (تمثيل عددي للجمل)
# 4. ترميز التصنيفات إلى أرقام باستخدام LabelEncoder
encoder = LabelEncoder()
y = encoder.fit_transform(labels)  # تحويل التصنيفات إلى أرقام (مثلاً "greeting" -> 0، "question" -> 1)
# 5. اختيار نموذج التدريب (هنا اخترنا MLPClassifier)
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
# تدريب النموذج باستخدام البيانات
model.fit(X, y)
# 6. إعداد ردود الشات بوت

responses = {
    "greetings": [
        "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening", "Howdy", "Greetings",
        "What's up?", "How's it going?", "How are you?", "Nice to see you", "Long time no see",
        "Yo", "Hi there", "Hey there", "Hello there", "Good to see you", "Welcome", "How have you been?"
    ],
    "thanks": [
        "Thank you", "Thanks", "Thanks a lot", "Thanks so much", "Many thanks", "I appreciate it", 
        "I’m grateful", "I’m thankful", "Thanks a ton", "Thanks a million", "I can’t thank you enough", 
        "Much appreciated", "I owe you one", "Thanks for everything", "I really appreciate it", 
        "I’m really grateful", "I appreciate your help", "Thanks for your support", "Thank you so much", 
        "Thanks for all you’ve done", "Thank you very much", "Thanks a bunch", "Thanks a great deal", 
        "Thanks heaps", "I truly appreciate it", "Thanks a lot for that", "I appreciate your kindness", 
        "You’re the best", "I’m deeply thankful", "Thank you kindly", "Thanks for your time", 
        "Thank you for your help", "I can’t express how thankful I am", "I appreciate this more than you know"
    ],
    "questions": [
        "How are you?", "What’s up?", "How’s it going?", "What’s your name?", "Where are you from?", 
        "How do you do?", "What do you do?", "Where do you live?", "How old are you?", "What’s your phone number?", 
        "Do you have any plans?", "What time is it?", "How can I help you?", "Are you okay?", 
        "What’s the weather like?", "What’s your favorite color?", "How was your day?", "Can I assist you with something?", 
        "Where is the nearest store?", "What are you doing?", "Do you need help?", "What’s the best way to get there?", 
        "Can you tell me about yourself?", "What do you think?", "How much does it cost?", "Why did you choose that?", 
        "What’s the matter?", "Have you heard about this?", "What’s on your mind?", "Are you hungry?", 
        "Would you like some help?", "How do you feel about that?", "Can you explain that again?", 
        "Do you want to join us?", "What do you like to do in your free time?", "How do you prefer to spend your weekends?"
    ],
    "help_requests": [
        "Can you help me?", "I need help", "Could you assist me?", "Can you give me a hand?", "Please help me", 
        "I need some assistance", "Can you help with this?", "I could use some help", "I need your help", 
        "Would you mind helping me?", "Can you show me how?", "Could you help me out?", "Please assist me", 
        "I’m stuck, can you help?", "I need some guidance", "Can you help me solve this?", "Could you lend a hand?", 
        "I need a little help here", "Can you do me a favor?", "Can you help me with this problem?", 
        "Would you help me out?", "I’m having trouble, can you assist?", "Could you give me some advice?", 
        "Can you help me figure this out?", "I’m in a bit of a jam, can you help?", "I need help with something", 
        "Can you help me understand?", "Would you be able to help?", "Can you please guide me?", "Can you help me get this done?", 
        "Could you assist me with this task?", "Please lend me a hand", "Can you help me make this decision?"
    ],
    "farewells": [
        "Goodbye", "Bye", "See you", "Take care", "See you later", "Farewell", "Catch you later", 
        "Until next time", "Have a good day", "Take it easy", "Goodbye for now", "I’ll see you soon", 
        "See you soon", "See you around", "Have a great day", "Good night", "Bye for now", "Talk to you later", 
        "Until we meet again", "Have a good one", "Later", "Adios", "Cya", "I’ll catch you later", 
        "Enjoy the rest of your day", "Goodbye, take care", "Have a nice day", "Take care of yourself", 
        "So long", "Goodbye, my friend", "Catch you on the flip side", "See you when I see you", 
        "Stay safe", "Don’t be a stranger", "Goodbye and take care", "I’ll  be seeing you", "Until we meet again", 
        "It was nice seeing you", "See you soon, take care", "See you at the next meeting", "Have a great evening", 
        "Hope to see you soon", "Take care, stay safe"
    ]
 }
     



# خريطة تربط التصنيفات بالمفاتيح داخل responses

# Intent Mapping
intent_mapping = {
    "greeting": "greetings",
    "question": "questions",
    "farewell": "farewells",
    "thanks": "thanks",
    "help": "help_requests"
}

# إعداد العمليات الحسابية
ops = {
    "plus": operator.add,
    "minus": operator.sub,
    "times": operator.mul,
    "multiplied by": operator.mul,
    "divided by": operator.truediv,
    "over": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "multiply": operator.mul,
    "divide": operator.truediv,
    "زائد": operator.add,
    "ناقص": operator.sub,
    "ضرب": operator.mul,
    "في": operator.mul,
    "على": operator.truediv
}

# تعريف sentiment-analyzer (من مكتبة transformers)
sentiment_analyzer = pipeline("sentiment-analysis")

# ذاكرة المحادثة
memory = {
    "name": None,
    "last_intent": None,
    "last_sentiment": None
}

# سجل المحادثات والتذكيرات
conversation_history = []
reminders = []

# دالة الترحيب بناءً على الوقت
def time_based_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning! ☀️"
    elif hour < 18:
        return "Good afternoon! 🌤️"
    else:
        return "Good evening! 🌙"

# دالة لتحسين الاستفسارات
def enhance_query(query):
    query = query.lower().strip()
    stopwords = [
        "please", "kindly", "could you", "would you", "i want to know", 
        "i would like to know", "can you tell me", "what is", "tell me", "do you know"
    ]
    for stopword in stopwords:
        query = query.replace(stopword, "")
    query = re.sub(r'[^\w\s]', '', query)
    query = ' '.join(query.split())
    return query

# دالة للبحث في Google
def search_google(query):
    api_key = "AIzaSyB-udyagZDYxqTFUKiMkZ4CmAry6Xi1ahQ"
    cse_id = "a7c519e7eb1e24186"
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {"q": query, "key": api_key, "cx": cse_id, "num": 1}
    response = requests.get(url, params=params)
    data = response.json()
    if "items" in data:
        snippet = data["items"][0]["snippet"]
        link = data["items"][0]["link"]
        return f"🔎 {snippet}\nLink: {link}"
    return "I couldn't find any results for this question."

# دالة للتحقق من التحية
def is_greeting(user_input):
    greetings = ["hi", "hello", "hey", "greetings", "howdy", "salut", "morning", "evening"]
    return any(word in user_input.lower() for word in greetings)

# دالة للتحقق من الشكر
def is_thanks(user_input):
    thanks_words = ["thanks", "thank you", "thx", "much appreciated", "thanks a lot", "ty",
                    "شكرا", "أشكرك", "مشكور", "ممتن", "جزاك الله خير", "شكرًا جزيلًا", "ألف شكر"]
    user_input = user_input.lower()
    return any(word in user_input for word in thanks_words)

# دالة للتحقق من السؤال
def is_question(user_input):
    question_words = ['what', 'who', 'how the', 'where', 'why', 'does', 'is', 'are', 'do', 'did', 'how long', 'how often', 'why']
    return any(word in user_input.lower() for word in question_words) or user_input.strip().endswith('?')

# دالة لاستخراج الاسم
def extract_name(user_input):
    text = user_input.lower()
    if "my name is" in text:
        return user_input.split("my name is")[-1].strip().capitalize()
    elif "اسمي" in text:
        return user_input.split("اسمي")[-1].strip().capitalize()
    return None

# دالة للحصول على حالة الطقس
def get_weather(city):
    api_key = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ar"
    response = requests.get(url)
    data = response.json()
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city}: {temp}°C, {desc}"
    return "لم أتمكن من العثور على معلومات الطقس."

# دالة لترجمة النص
def translate_text(text, dest='ar'):
    try:
        return GoogleTranslator(source='auto', target=dest).translate(text)
    except Exception as e:
        return "حدث خطأ أثناء الترجمة."

# دالة لإضافة تذكير
def add_reminder(text):
    reminders.append({"text": text, "time": datetime.now()})
    return f"⏰ تم تذكيرك: {text}"

# دالة للتحقق من التكرار
def detect_repetition(user_input):
    return any(user_input == entry["user"] for entry in conversation_history[-3:])

# دالة لإجابة مخصصة
def custom_response(user_input):
    name = extract_name(user_input)
    if name:
        memory["name"] = name
        return f"Nice to meet you, {memory['name']}! 👋"

    if "what is my name" in user_input.lower() or "ما هو اسمي" in user_input.lower():
        if memory["name"]:
            return f"Your name is {memory['name']}! 🌟"
        else:
            return "I don't know your name yet. Tell me by saying 'My name is ...'"

    if "who made you" in user_input.lower() or "من صنعك" in user_input.lower():
        return "I was created by Dev12."

    if "weather in" in user_input.lower():
        city = user_input.lower().split("weather in")[-1].strip()
        return get_weather(city)

    if user_input.lower().startswith("translate "):
        phrase = user_input[9:]
        return f"🔁 الترجمة: {translate_text(phrase)}"

    if user_input.lower().startswith("remind me to"):
        task = user_input[12:].strip()
        return add_reminder(task)

    if user_input.lower() in ["how are you"]:
        return "I am fine, thank you! 😊"

    return None

# دالة لحساب المعادلات
def calculate_expression(user_input):
    user_input = user_input.lower()
    pattern_en = r'(\d+)\s*(plus|minus|times|multiplied by|divided by|over|\+|\-|\*|/)\s*(\d+)'
    match = re.search(pattern_en, user_input)
    if match:
        n1, op, n2 = int(match[1]), match[2], int(match[3])
        if op in ops:
            return f"The result is {ops[op](n1, n2)}"
    pattern_ar = r'(\d+)\s*(زائد|ناقص|ضرب|في|على)\s*(\d+)'
    match_ar = re.search(pattern_ar, user_input)
    if match_ar:
        n1, op, n2 = int(match_ar[1]), match_ar[2], int(match_ar[3])
        if op in ops:
            return f"The result is {ops[op](n1, n2)}"
    try:
        result = eval(user_input, {"__builtins__": None}, {})
        return f"🔢 الناتج: {result}"
    except:
        return None

# دالة للشات بوت
def chatbot_reply(user_input):
    sentiment = sentiment_analyzer(user_input)[0]
    memory["last_sentiment"] = sentiment["label"]

    if detect_repetition(user_input):
        return "🤔 لقد قلت هذا مسبقًا، هل يمكنك التوضيح أكثر؟"

    if is_greeting(user_input):
        return f"{random.choice(['Hello', 'Hey', 'Hi'])} {memory['name'] or ''}!".strip()

    if is_thanks(user_input):
        return f"You're welcome {memory['name'] or ''}! 😊".strip()

    custom = custom_response(user_input)
    if custom:
        return custom

    calc = calculate_expression(user_input)
    if calc:
        return calc

    if is_question(user_input):
        enhanced_query = enhance_query(user_input)
        return search_google(enhanced_query)

    return "I didn't understand, can you rewrite your question?"


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    try:
        reply = chatbot_response(user_message)  # نفترض وجود الدالة بهذا الاسم في EGYchat
    except Exception as e:
        reply = f"Error: {str(e)}"
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
