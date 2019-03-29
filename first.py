import re

def title_case(title, minor_words=None):
    if not minor_words:
        return title.title()
    else:
        splited_title = re.split("\\s", title.title())
        splited_minor_words = re.split("\\s",minor_words.lower())
        new_title = splited_title[0]
        for s in splited_title[1:]:
            if (s.lower() in splited_minor_words):
                new_title+=str(' '+s.lower())
            else:
                new_title+=str(' '+s)
        return new_title

if __name__ == "__main__":
    print title_case('a clash of KINGS','a an the of')
    print title_case('THE WIND IN THE WILLOWS', 'The In')
    print title_case('the quick brown fox')