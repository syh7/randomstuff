from enum import Enum


class Chance(Enum):
    START = 'Go to Start. Collect €200.'
    RAIL1 = 'Go to the nearest railroad and pay the owner twice the rent. If the property is unowned, you are free to ' \
            'buy it from the bank. '
    RAIL2 = 'Go to the nearest railroad and pay the owner twice the rent. If the property is unowned, you are free to ' \
            'buy it from the bank. '
    DIVIDEND = 'Bank pays you dividend of €50.'
    JAIL = 'You were caught mining Russiacoin. Go to jail. Do not pass Start, do not receive 200.'
    FREE = 'This is a get out of jail free card.'
    BACK = 'Go back three spaces.  Three shall be the number thou shalt count, and the number of the counting shall ' \
           'be three. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. ' \
           'Five is right out. Once the number three, being the third number, be reached, then thou shalt stop.'
    REPAIRS = 'Make general repairs on all your property: €25 for each house, €100 for each hotel.'
    TAX = 'Pay poor tax of €15.'
    READING = 'Take a trip to Reading Railroad. If you pass Start, collect €200. If the railroad is owned, pay rent.'
    BOARDWALK = 'Take a walk on Boardwalk.'
    CHAIRMAN = 'You have been elected Chairman of the Board. Pay each player €50.'
    BUILDING = 'Your building and loan matures. Collect €150.'
    CROSSWORD = 'You have won a crossword puzzle. Collect €100.'


class Community(Enum):
    START = 'Go to Start. Collect €200.'
    BANK = 'Bank error in your favor. Collect €200.'
    DOCTOR = 'Doctor\'s fee. Pay €50.'
    JAIL = 'You were caught mining Russiacoin. Go to jail. Do not pass Start, do not receive 200.'
    FREE = 'This is a get out of jail free card.'
    STOCK = 'From sale of stock, you get €50.'
    OPERA = 'Grand Opera Night. Collect €50 from every player for opening night seats.'
    XMAS = 'Holiday fund matures. Collect €100.'
    TAX = 'Income tax refund. Collect €20.'
    BIRTHDAY = 'It\'s your birthday today! All other players will give you €20.'
    INSURANCE = 'Life insurance matures. Collect €100.'
    HOSPITAL = 'Pay hospital fees of €100.'
    SCHOOL = 'Pay school fees of €150.'
    CONSULT = 'Collect €25 consultancy fee.'
    REPAIRS = 'You are assessed for street repairs. For each house, pay €40. For each hotel, pay €115.'
    BEAUTY = 'You have won second prize in a beauty contest. Collect €10.'
    HERITAGE = 'You inherit €100.'
