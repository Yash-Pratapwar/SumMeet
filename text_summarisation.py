from unittest.util import _MAX_LENGTH
import torch
import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small', model_max_length = 1000)
device = torch.device('cpu')

file = open('transcripted_files/yt_transcript.txt', 'r')
text = file.read()
# text ="""
# The US has "passed the peak" on new coronavirus cases, President Donald Trump said and predicted that some states would reopen this month.
# The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world.
# At the daily White House coronavirus briefing on Wednesday, Trump said new guidelines to reopen the country would be announced on Thursday after he speaks to governors.
# "We'll be the comeback kids, all of us," he said. "We want to get our country back."
# The Trump administration has previously fixed May 1 as a possible date to reopen the world's largest economy, but the president said some states may be able to return to normalcy earlier than that.
# """


preprocess_text = text.strip().replace("\n","")
t5_prepared_Text = "summarize: "+preprocess_text
print ("original text preprocessed: \n", preprocess_text)

tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt",  truncation = False).to(device)


# summmarize 
summary_ids = model.generate(tokenized_text,  # type: ignore
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=40,
                                    max_length=100,
                                    early_stopping=True)

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print ("\n\nSummarized text: \n",output)
