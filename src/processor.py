from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    def analyse(text: str) -> str:
        ...

class ProcessorImpl(Processor):
    def analyse(self, text: str) -> str: 
        #raise NotImplementedError
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.lower()
        text = text.split(" ")

        frequency_occurrence = {}

        for word in text:
            if word in frequency_occurrence:
                frequency_occurrence[word] += 1
                continue                
            frequency_occurrence[word] = 1

        n_words = len(frequency_occurrence)     #TODO: check, it's wrong

        frequency_occurrence_ordered = sorted(frequency_occurrence.items(), key=lambda x: x[1], reverse=True)

        # most_frequent_word = ""
        # n_appereances_most_frequent_word = 0     

        # for word, n_appereances in frequency_occurrence.items():
        #     if n_appereances >= n_appereances_most_frequent_word:
        #         most_frequent_word = word
        #         n_appereances_most_frequent_word = n_appereances

        top_ten = ""
        current_word_ranking = 0
        for word, n_appereances in frequency_occurrence_ordered:
            current_word_ranking+=1
            if current_word_ranking <= 10:
                top_ten += " " + str(current_word_ranking)+". "+word              

        return f"Those are the top 10 words used:" + top_ten + ". The text has in total {n_words} words"
        # return most_frequent_word         