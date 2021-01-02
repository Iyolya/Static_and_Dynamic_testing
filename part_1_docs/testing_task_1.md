### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
                                          #1 Missing __init__.py constructor

  def check_for_ace(self, card):
    if card.value = 1:                    #2 Assignment operator ' = ' being used instead of
                                          # comparison operator ' == '
      return True
    else                                  #3 Missing colon after 'else'
      return False
   

  dif highest_card(self, card1 card2):    #4 'def' keyword misspelled  #5 Missing comma after
                                                                       # 'card1' 
  if card1.value > card2.value:           #6 Missing indentation on line30-line33
    return card                           #7 Variable should be 'card1' not 'card'
  else:
    return card2
  


def cards_total(self, cards):
  total                                   #8 'total' variable is not defined
  for card in cards:
    total += card.value
    return "You have a total of" + total  #9 syntax error in f-string 
    #                                     # should be: f"You have a total of {total}" 
  
```
