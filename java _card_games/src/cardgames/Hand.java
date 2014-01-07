/**
 * Hand containing standard poker cards
 */
package cardgames;

import java.util.ArrayList;

/**
 * @author clee2
 *
 */
public class Hand {
	String name;
	Integer limit;
	ArrayList<Card> hand;

	//Public Constructor
	public Hand(String name, Integer limit){
		//Card limit -1 for infinite
		this.name = name;
		this.limit = limit==-1?52:limit; //If limit == -1 then 52 else just limit
		this.hand = new ArrayList<Card> ();
	}
	
	//Add a card to the hand
	public void addCard(Card card){
		this.hand.add(card);
	}
	
	//Remove card from hand
	public void removeCard(Card card){
		this.hand.remove(card);
	}
	
	//Print cards in hand
	public void print(){
		for (Card card: this.hand){
			card.print();
		}
	}
}
