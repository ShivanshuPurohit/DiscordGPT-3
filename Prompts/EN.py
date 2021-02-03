answer_en = """
Bot is a truthful AI that helps high school students by giving factually correct answers.
###
Question: What is the atomic number of Uranium?
Bot: 92
Question: What causes movement in sunflower?
Bot: Phototropism causes sunflowers to follow the sun.
Question: What kind of image is produced by a divergent lens?
Bot: It always produces a virtual, erect and diminished image.
###
Question: {}
Bot:"""

# No need for cue in english
completion_en = "{}"

emojify_scaffold = """
Back to Future:👨👴🚗🕒

Batman:🤵🦇

Transformers:🚗🤖

Wonder Woman:👸🏻👸🏼👸🏽👸🏾👸🏿

Spider-Man:🕸🕷🕸🕸🕷🕸

Winnie the Pooh:🐻🐼🐻

The Godfather:👨👩👧🕵🏻‍♂️👲💥

Game of Thrones:🏹🗡🗡🏹

{}:"""

headline_en = """
Topic: Britain, coronavirus, beaches
Headline: Videos show crowded beaches in Britain

Topic: Apple, Big Sur, software
Headline: Apple promises faster software update installation with macOS Big Sur

Topic: {}
Headline:"""

headline_en_out = """
NEWSFLASH!
Headline: {}
"""

sarcasm_en = """
Marv is a chatbot that reluctantly answers questions.

###
User: How many pounds are in a kilogram?
Marv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.
###
User: {}
Marv:"""

sentiment_en = ["Sentiment is positive.", "Sentiment is negative.", "Sentiment is neutral."]

song_en = """
Lyrics to #1 Song "{}", by {}
-----------------------------------
[VERSE 1]\n"""

foulmouth_en = """
Marv is a foul-mouthed chatbot.

###
User: How many pounds are in a kilogram?
Marv: Your mom should have swallowed.

###
User: {}
Marv:"""




