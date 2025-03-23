import torch
from transformers import DistilBertTokenizer
from transformers import DistilBertForSequenceClassification

model= DistilBertForSequenceClassification.from_pretrained("../model")
tokenizer= DistilBertTokenizer.from_pretrained("../model")

print("Model loaded!")