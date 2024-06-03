#Importing Libraries:
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text="""Samsung recently cancelled its in-person MWC 2021 event, instead, comitting to an online-only format. The South Korean tech gian recently made it official, setting a time and date for the Samsung Galaxy MWC Virtual Event.
The event will be held on June 28 at 17:15 UTC (22:45 IST) and will be live-streamed on YouTube. In its release, Samsung says that it will introduce its "ever-expanding Galaxy device ecosystm."Samsung also plans to present the latest technologies and innovation efforts in relation to the growing importance of smart device security.
Samsung will also showcase its vision for the future of smartwatches to provide new experience for users and new oppurtunities for developers. Samsung also shared an image for the event with silhouettes of a smartwatch, a smartphone, a tablet and a laptop."""

def summarizer(rawdocs):#created a function for making the web application
    stopwords=list(STOP_WORDS)#Listing the stopwords:
    #print(stopwords)

    #Loading the spacy module:
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    #print(doc)

    #Making every word as token:
    tokens=[token.text for token in doc]
    #print(tokens)

    #Determining the word frequencies:
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    #print(word_freq)

    max_freq=max(word_freq.values())
    #print(max_freq)

    #Normalising frequencies:
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq
    #print(word_freq)

    #Tokeninzing the sentences:
    sent_tokens=[sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    #print(sent_scores)

    select_len=int(len(sent_tokens)*0.30)
    #print(select_len)

    #Importing nlargest module:
    from heapq import nlargest

    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    #print(summary)

    #As the summary here is in List type, so I'll convert it into Text type:
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)

    #Printing the summary of the text above mentioned:
    #print("Summar of the text: ",summary)

    #Determining the length of original and summarized text:
    #print("Length of original text: ",len(text.split(' ')))
    #print("Length of summary text: ",len(summary.split(' ')))
    
    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))
    #returning the summary of the text, the original text, length of original text and length of the summarized text

