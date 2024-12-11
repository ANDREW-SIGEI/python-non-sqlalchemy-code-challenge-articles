#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :slightly_smiling_face: let's debug :vibing_potato:")

author1 = Author("Carry Bradshaw")
author2 = Author("Nathaniel Hawthorne")

magazine1 = Magazine("Vogue", "Fashion")
magazine2 = Magazine("AD", "Architecture")

article1 = Article(author1, magazine1, "How to wear a tutu with style")
article2 = Article(author1, magazine2, "2023 Eccentric Design Trends")
article3 = Article(author2, magazine1, "Carra Marble is so 2020")


# don't remove this line, it's for debugging!
ipdb.set_trace()