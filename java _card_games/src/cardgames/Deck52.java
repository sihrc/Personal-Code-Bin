/**
 * Standard 52 Deck of cards
 */
package cardgames;

import java.util.ArrayList;
import java.util.HashSet;

/**
 * @author clee2
 *
 */
public class Deck52 {
	ArrayList<Card> deck;
	public Deck52(){
		this.deck = new ArrayList<Card>();
		for (int card = 1; card <= 13; card++){
			this.deck.add(new Card(card, Card.SPADES));
			this.deck.add(new Card(card, Card.HEARTS));
			this.deck.add(new Card(card, Card.DIAMONDS));
			this.deck.add(new Card(card, Card.CLUBS));
		}
		shuffle();
	}
	
	//Shuffles the deck
	public void shuffle(){
		HashSet<Card> shuffler = new HashSet<Card> ();
		shuffler.addAll(this.deck);
		this.deck.clear();
		this.deck.addAll(shuffler);
	}
	
	//Draw Cards
	public ArrayList<Card> dealCards(int n){
		ArrayList<Card> drawn = new ArrayList<Card> ();
		for (int i = 0; i < n; i++){
			drawn.add(this.deck.get(0));
			this.deck.remove(0);
		}
		return drawn;
	}
	
	//Return Cards
	public void returnCards(ArrayList<Card> returned){
		this.deck.addAll(returned);
	}
}
