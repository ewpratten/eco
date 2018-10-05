import sys
from random import randint
from time import sleep

def file_len(fname):
    with open(fname) as f:
        return sum(1 for line in f)

print("ECO c/cpp compiler")
print("Version 1.0")

if len(sys.argv) <= 1:
    print("Compiled Nothing Successfully.")
    print("Please pass in a file path to ensure failure.")
    exit(1)

print("compiling...\n")

# wait random amount of time

sleep(randint(1,10))

#throw random error from list
errors = [
        "The compiler dislikes your code style",
        "File too short",
        "Too many semicolons",
        "Not enough semicolons",
        "Minimum recursion depth not met",
        "418 - I'm a teapot",
        "//TODO: add useful error message",
        "Really? this counts as code to you? Try again.",
        "The compiler wrongfully decided that this line was not needed and removed it",
        "At-least-once delivery has failed to deliver the error message at least once",
        "No overflow detected. Please use larger numbers",
        "Maximum line length of 1 exceeded.",
        "Variable name too descriptive"
        """You can't parse [X]HTML with regex. Because HTML can't be parsed by regex. 
        Regex is not a tool that can be used to correctly parse HTML. 
        As I have answered in HTML-and-regex questions here so many times before, 
        the use of regex will not allow you to consume HTML. 
        Regular expressions are a tool that is insufficiently sophisticated to understand the constructs employed by HTML. 
        HTML is not a regular language and hence cannot be parsed by regular expressions. 
        Regex queries are not equipped to break down HTML into its meaningful parts. 
        so many times but it is not getting to me. 
        Even enhanced irregular regular expressions as used by Perl are not up to the task of parsing HTML. 
        You will never make me crack. 
        HTML is a language of sufficient complexity that it cannot be parsed by regular expressions. 
        Even Jon Skeet cannot parse HTML using regular expressions. 
        Every time you attempt to parse HTML with regular expressions, the unholy child weeps the blood of virgins, and Russian hackers pwn your webapp.
        Parsing HTML with regex summons tainted souls into the realm of the living. 
        HTML and regex go together like love, marriage, and ritual infanticide.
        The <center> cannot hold it is too late. 
        The force of regex and HTML together in the same conceptual space will destroy your mind like so much watery putty.
        If you parse HTML with regex you are giving in to Them and their blasphemous ways which doom us all to inhuman toil for the One whose Name cannot be expressed in the Basic Multilingual Plane, he comes.
        HTML-plus-regexp will liquify the n​erves of the sentient whilst you observe, your psyche withering in the onslaught of horror.
        Rege̿̔̉x-based HTML parsers are the cancer that is killing StackOverflow it is too late it is too late we cannot be saved the trangession of a chi͡ld ensures regex will consume all living tissue (except for HTML which it cannot, as previously prophesied) dear lord help us how can anyone survive this scourge using regex to parse HTML has doomed humanity to an eternity of dread torture and security holes using regex as a tool to process HTML establishes a breach between this world and the dread realm of c͒ͪo͛ͫrrupt entities (like SGML entities, but more corrupt) a mere glimpse of the world of reg​ex parsers for HTML will ins​tantly transport a programmer's consciousness into a world of ceaseless screaming, he comes, the pestilent slithy regex-infection wil​l devour your HT​ML parser, application and existence for all time like Visual Basic only worse he comes he comes do not fi​ght he com̡e̶s, ̕h̵i​s un̨ho͞ly radiańcé destro҉ying all enli̍̈́̂̈́ghtenment, HTML tags lea͠ki̧n͘g fr̶ǫm ̡yo​͟ur eye͢s̸ ̛l̕ik͏e liq​uid pain, the song of re̸gular exp​ression parsing will exti​nguish the voices of mor​tal man from the sp​here I can see it can you see ̲͚̖͔̙î̩́t̲͎̩̱͔́̋̀ it is beautiful t​he final snuffing of the lie​s of Man ALL IS LOŚ͖̩͇̗̪̏̈́T ALL I​S LOST the pon̷y he comes he c̶̮omes he comes the ich​or permeates all MY FACE MY FACE ᵒh god no NO NOO̼O​O NΘ stop the an​*̶͑̾̾​̅ͫ͏̙̤g͇̫͛͆̾ͫ̑͆l͖͉̗̩̳̟̍ͫͥͨe̠̅s ͎a̧͈͖r̽̾̈́͒͑e n​ot rè̑ͧ̌aͨl̘̝̙̃ͤ͂̾̆ ZA̡͊͠͝LGΌ ISͮ̂҉̯͈͕̹̘̱ TO͇̹̺ͅƝ̴ȳ̳ TH̘Ë͖́̉ ͠P̯͍̭O̚​N̐Y̡ H̸̡̪̯ͨ͊̽̅̾̎Ȩ̬̩̾͛ͪ̈́̀́͘ ̶̧̨̱̹̭̯ͧ̾ͬC̷̙̲̝͖ͭ̏ͥͮ͟Oͮ͏̮̪̝͍M̲̖͊̒ͪͩͬ̚̚͜Ȇ̴̟̟͙̞ͩ͌͝S̨̥̫͎̭ͯ̿̔̀ͅ
        -------------------------=
        Please, write quality code."""
        ]

random_line = randint(1, file_len(sys.argv[1]))

print("Error on line: " + str(random_line))
print(errors[randint(0, len(errors) - 1)])

# exit code one
exit(1)
