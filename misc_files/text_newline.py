file_name = 'short'
text = " Somebody didn't get the memo. It's not happening with me. How can I do it? You update your zoom. It's updated. He is trying to make a move. Thakur, this is the podcast going forward. You know this right? All the listeners on Spotify and Apple, you have to head on to the YouTube channel."
s_n = ''.join(text.replace('.','\n'))
print(s_n)
with open('summeet_package/transcripted_files/'+file_name+'.txt', 'w') as file:
        file.writelines(s_n)