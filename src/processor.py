from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    def analyse(text: str) -> str:
        ...

class ProcessorImpl(Processor):
    def analyse(self, text: str) -> str: 
        #raise NotImplementedError
        text = self._clean_text(text)
        frequency_occurrence = self._frequency_occurrence(text)      
        total_words = len(frequency_occurrence)
        top_ten = self._top_ten(frequency_occurrence)               
        return f"Those are the top 10 words used: {top_ten}. The text has in total {total_words} words"

    def _clean_text(self, text: str) -> str:
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.lower()
        text = text.split(" ")
        return text
    
    def _frequency_occurrence(self, text: str) -> dict:
        frequency_occurrence = {}

        for word in text:
            if word in frequency_occurrence:
                frequency_occurrence[word] += 1
                continue                
            frequency_occurrence[word] = 1

        return frequency_occurrence
    
    def _top_ten(self, frequency_occurrence: dict) -> str:
        frequency_occurrence_ordered = sorted(frequency_occurrence.items(), key=lambda x: x[1], reverse=True)

        top_ten = ""
        current_word_ranking = 0
        for word, _ in frequency_occurrence_ordered:
            current_word_ranking+=1
            if current_word_ranking <= 10:
                top_ten += " " + str(current_word_ranking)+". "+word   

        return top_ten
