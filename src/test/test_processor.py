from processor import ProcessorImpl


class TestProcessor:
    def test_it_returns_most_common_words(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

        actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

        expected_analysis = "Those are the top 10 words used: 1. you 2. this 3. your 4. to 5. text 6. test 7. should 8. practice 9. make 10. it. The text has in total 21 words"
        assert actual_analysis == expected_analysis

    def test_it_returns_the_most_common_word(self):
        sentence_to_proccess = "Hello, this is an example for you to practice. You should grab this text and make it as your test case."

        actual_analysis = ProcessorImpl().analyse(sentence_to_proccess)

        expected_analysis = "you"
        assert actual_analysis == expected_analysis