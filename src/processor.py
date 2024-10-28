from abc import ABC, abstractmethod
import math
import re


class Processor(ABC):
    @abstractmethod
    def analyse(text: str) -> str:
        ...

class ProcessorImpl(Processor):
    TOP_TEN: int = 10

    def analyse(self, text: str) -> str: 
        #raise NotImplementedError
        filtered_text = self._remove_code_snippet(text)
        clean_text = self._clean_text(filtered_text)
        
        frequency_occurrence = self._frequency_occurrence(clean_text)   
        top_ten = self._top_ten(frequency_occurrence)               
        
        total_words = len(clean_text)
        return f"Those are the top 10 words used: {top_ten}. The text has in total {total_words} words"

    def get_time_to_read(self, text: str) -> dict:
        clean_text = self._clean_text(text)
        
        number_of_words = len(clean_text)
        words_per_minute = number_of_words/200
        decimal_points, minutes = math.modf(words_per_minute)
        
        return {
            "minutes": minutes,
            "seconds": round(decimal_points*0.6*100)
        }

    def _remove_code_snippet(self, text):
        return re.sub(r'` ` `.*?` ` `', '', text)

    def _clean_text(self, text: str) -> str:
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace(":", "")
        text = text.lower()
        text = text.strip()
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
        frequency_occurrence_ordered = self._sort_by_occurrence_descendent(frequency_occurrence)

        top_ten = ""
        current_word_ranking = 0
        for word, _ in frequency_occurrence_ordered:
            current_word_ranking+=1
            if current_word_ranking <= self.TOP_TEN:
                top_ten += " " + str(current_word_ranking)+". "+word   

        return top_ten

    def _sort_by_occurrence_descendent(self, frequency_occurrence):
        return sorted(frequency_occurrence.items(), key=lambda x: x[1], reverse=True)    