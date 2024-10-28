from processor import ProcessorImpl


class TestProcessor:
    def test_it_returns_most_common_words(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

        actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

        expected_analysis = "Those are the top 10 words used:  1. this 2. you 3. hello 4. is 5. an 6. example 7. for 8. to 9. practice 10. should. The text has in total 21 words"
        assert actual_analysis == expected_analysis


    def test_it_return_how_much_time_takes_the_text_to_be_read(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

        actual_analysis = ProcessorImpl().get_time_to_read(sentence_to_proccess)

        expected_analysis = {
            "minutes": 0,
            "seconds": 6
        }
        assert actual_analysis == expected_analysis
    
    def test_it_analyse_the_text_ignoring_code_snippets(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case: ` ` `javascript if (true) {console.log('should should should')}` ` `"

        actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

        expected_analysis = "Those are the top 10 words used:  1. this 2. you 3. hello 4. is 5. an 6. example 7. for 8. to 9. practice 10. should. The text has in total 21 words"
        assert actual_analysis == expected_analysis