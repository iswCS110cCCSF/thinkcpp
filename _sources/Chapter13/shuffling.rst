
.. _shuffling:

Shuffling
---------

For most card games you need to be able to shuffle the deck; that is,
put the cards in a random order. In :numref:`random` we
saw how to generate random numbers, but it is not obvious how to use
them to shuffle a deck.

One possibility is to model the way humans shuffle, which is usually by
dividing the deck in two and then reassembling the deck by choosing
alternately from each deck. Since humans usually don’t shuffle
perfectly, after about 7 iterations the order of the deck is pretty well
randomized. But a computer program would have the annoying property of
doing a perfect shuffle every time, which is not really very random. In
fact, after 8 perfect shuffles, you would find the deck back in the same
order you started in. For a discussion of that claim, see
``http://www.wiskit.com/marilyn/craig.html`` or do a web search with the
keywords “perfect shuffle.”

A better shuffling algorithm is to traverse the deck one card at a time,
and at each iteration choose two cards and swap them.

Here is an outline of how this algorithm works. To sketch the program, I
am using a combination of C++ statements and English words that is
sometimes called **pseudocode**:

::

     for (size_t i = 0; i < cards.size(); i++) {
       // choose a random number between i and cards.size()
       // swap the ith card and the randomly-chosen card
     }

The nice thing about using pseudocode is that it often makes it clear
what functions you are going to need. In this case, we need something
like ``randomInt``, which chooses a random integer between the
parameters ``low`` and ``high``, and ``swapCards`` which takes two
indices and switches the cards at the indicated positions.

.. index::
   single: pseudocode

.. note::
   If you are even the slightest bit unsure on how to begin coding
   your program, **pseudocode** is a great place to start!

You can probably figure out how to write ``randomInt`` by looking at
:numref:`random`, although you will have to be careful
about possibly generating indices that are out of range.

You can also figure out ``swapCards`` yourself. I will leave the
remaining implementation of these functions as an exercise to the
reader.

.. mchoice:: shuffling_1
   :answer_a: cstdlib
   :answer_b: iostream
   :answer_c: strings
   :answer_d: cmath
   :correct: a
   :feedback_a: Correct!
   :feedback_b: This is the library for streaming std::cin and cout.
   :feedback_c: This is the library for strings.
   :feedback_d: This is the library for math functions.

   Which library should we include to create random numbers?

.. activecode:: shuffling_2
   :language: cpp
   :compileargs: [ '-Wall', '-Werror' ]

   Try writing the ``randomInt`` and ``swapCards`` functions in the commented sections
   of the active code below. Once you're done with ``randomInt`` and ``swapCards``,
   try using them to implement the ``Deck`` member function ``shuffleDeck``. If done correctly,
   the program should output a shuffled deck of cards. If you stuck, you can reveal the 
   extra problems at the end for help. 
   ~~~~
   #include <iostream>
   #include <string>
   #include <vector>
   #include <cstdlib>
   using namespace std;

   enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES };

   enum Rank { ACE=1, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,
   TEN, JACK, QUEEN, KING };

   int randomInt (int low, int high) {
       // ``randomInt`` should choose a random integer between
       // the low and high parameters and return an integer.
       // Delete the return 0 and write your implementation here.
       return 0;
   }

   struct Card {
       Rank rank;
       Suit suit;
       Card ();
       Card (Suit s, Rank r);
       void print () const;
   };

   struct Deck {
       vector<Card> cards;
       Deck ();
       void print () const;
       void swapCards (int index1, int index2);
       void shuffleDeck ();
   };

   void Deck::swapCards (int index1, int index2) {
       // ``swapCards`` should take two indices and switch the cards
       // at the indicated positions. Write your implementation here.
   }

   void Deck::shuffleDeck () {
       // Follow the pseudocode from above and use ``randomInt`` and 
       // ``swapCards`` to write the ``shuffle`` member function. 
       // Write your implementation here.
   }

   int main() {
       Deck deck;
       deck.shuffleDeck ();
       deck.print ();
   }

   ====
   Card::Card () {
       suit = SPADES;  rank = ACE;
   }

   Card::Card (Suit s, Rank r) {
       suit = s;  rank = r;
   }

   void Card::print () const {
       vector<string> suits (4);
       suits[0] = "Clubs";
       suits[1] = "Diamonds";
       suits[2] = "Hearts";
       suits[3] = "Spades";

       vector<string> ranks (14);
       ranks[1] = "Ace";
       ranks[2] = "2";
       ranks[3] = "3";
       ranks[4] = "4";
       ranks[5] = "5";
       ranks[6] = "6";
       ranks[7] = "7";
       ranks[8] = "8";
       ranks[9] = "9";
       ranks[10] = "10";
       ranks[11] = "Jack";
       ranks[12] = "Queen";
       ranks[13] = "King";

       cout << ranks[rank] << " of " << suits[suit] << endl;
   }

   Deck::Deck () {
       vector<Card> temp (52);
       cards = temp;

       int i = 0;
       for (Suit suit = CLUBS; suit <= SPADES; suit = Suit(suit+1)) {
           for (Rank rank = ACE; rank <= KING; rank = Rank(rank+1)) {
               cards[i].suit = suit;
               cards[i].rank = rank;
               i++;
           }
       }
   }

   void Deck::print () const {
       for (size_t i = 0; i < cards.size(); i++) {
           cards[i].print ();
       }
   }

.. reveal:: shuffle_reveal_1
   :showtitle: randomInt Help
   :hidetitle: Hide Problem

   .. parsonsprob:: shuffling_help_1
      :numbered: left
      :adaptive:

      Let's write the code for the randomInt function. randomInt should take two parameters,
      low and high, and return a random integer between them, inclusive.
      -----
      int randomInt (int low, int high) {
      =====
      int randomInt () {                         #paired
      =====
       int x = random ();
      =====
       int y = x % (high - low + 1) + low; 
      =====
       int y = x % high;                         #paired
      =====
       return y;
      }
      =====
       return x;                         #paired
      }

.. reveal:: shuffle_reveal_2
   :showtitle: swapCards Help
   :hidetitle: Hide Problem

   .. parsonsprob:: shuffling_help_2
      :numbered: left
      :adaptive:

      Let's write the code for the swapCards function. We'll write swapCards
      as a Deck member function that takes two indices as parameters.
      -----
      void Deck::swapCards (int index1, int index2) {
      =====
      void Card::swapCards (int index1, int index2) {                         #paired
      =====
       Card temp = cards[index1];
      =====
       cards[index1] = cards[index2]; 
      =====
       cards[index2] = cards[index1];                         #paired 
      =====
       cards[index2] = temp;
      }

.. reveal:: shuffle_reveal_3
   :showtitle: shuffleDeck Help
   :hidetitle: Hide Problem

   .. parsonsprob:: shuffling_help_3
      :numbered: left
      :adaptive:

      Let's write the code for the shuffleDeck function. We'll use randomInt
      and swapCards in our implementation of shuffleDeck.
      -----
      void Deck::shuffleDeck () {
      =====
      Deck Deck::shuffleDeck (Deck deck) {                         #paired
      =====
       for (size_t i = 0; i < cards.size(); i++) {
      =====
        int x = randomInt (i, cards.size() - 1); 
      =====
        int x = randomInt (i, cards.size());                         #paired 
      =====
        swapCards (i, x);
       }
      }

