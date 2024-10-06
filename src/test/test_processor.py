from processor import ProcessorImpl


class TestProcessor:
    def test_it_returns_most_common_words(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

        actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

        expected_analysis = "Those are the top 10 words used:  1. this 2. you 3. hello 4. is 5. an 6. example 7. for 8. to 9. practice 10. should. The text has in total 19 words"
        assert actual_analysis == expected_analysis

    # def test_it_returns_the_most_common_word(self):
    #     sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

    #     actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

    #     expected_analysis = "you"
    #     assert actual_analysis == expected_analysis