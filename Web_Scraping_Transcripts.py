import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = ['https://transcripts.fandom.com/wiki/Star_Wars_Episode_IV:_A_New_Hope',
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_V:_The_Empire_Strikes_Back',
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_VI:_Return_of_the_Jedi',
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_I:_The_Phantom_Menace',  
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_II:_Attack_of_the_Clones',  
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_III:_Revenge_of_the_Sith',  
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_VII:_The_Force_Awakens',
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_VIII:_The_Last_Jedi', 
        'https://transcripts.fandom.com/wiki/Star_Wars_Episode_IX:_The_Rise_of_Skywalker'] 

movies = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'The Force Awakens', 'The Last Jedi', 'The Rise of Skywalker']



def get_transcripts(url): 
    
    '''Returns transcript from transcripts.fandom.com.'''
    
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find_all('p')]
    return text

transcripts = [get_transcripts(u) for u in urls]

df = pd.DataFrame({'title': movies, 'transcript':transcripts})

df['transcript'] = [''.join(map(str, t)) for t in df['transcript']]  # converting transcripts from lists to strings

df.to_csv('star_wars_transcripts.csv',index=False)

