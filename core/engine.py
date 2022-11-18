import spacy
import nltk
import typing as t
import re


class Engine:
    def __init__(self, paragraph: str):
        self.nlp = spacy.load("en_core_web_sm")
        self.paragraph = paragraph


    def paragraph_to_list(self) -> t.List:
        tmp = self.paragraph.split(" .,;:'\"")
        return tmp


    def segment_sentence(self):
        doc = self.nlp(self.paragraph)
        assert doc.has_annotation("SENT_START")

        result = []

        for sent in doc.sents:
            result.append(sent.text)

        return result


    def get_pos(self, text: str) -> str:
        result = []
        doc = self.nlp(text)
        for token in doc:
            result.append([token, token.pos_])

        return result


    def get_subject(self):
        result = ""
        first = True

        for word in self.paragraph.split(" "):
            pos = self.nlp(word)[0].pos_
            result += word if first else " " + word
            first = False

            if pos == 'NOUN':
                return result

        raise ValueError("No subject found")


if __name__ == "__main__":
    sentence = "The quick brown keyboard jumps over the lazy dog. The keyboard broke my hands."
    a = Engine(sentence)
    # a.segment_sentence()
    # print(a.get_pos(sentence))

    print(a.get_subject())
