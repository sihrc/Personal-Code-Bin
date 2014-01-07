/**
 * Card Object
 * A standard poker card
 * Attributes:
 * 	- value
 * 	- suit
 */
package cardgames;

/**
 * @author clee2
 *
 */
public class Card {
	Integer value;
	String suit;
	
	//Standard Suits
	static final String SPADES = "spades";
	static final String HEARTS = "hearts";
	static final String CLUBS = "clubs";
	static final String DIAMONDS = "diamonds";
	
	//Public Constructor
	public Card(Integer value, String suit){
		assert (value > 13);
		this.value = value;
		this.suit = suit;
	}
	
	//String representation of this object
	public String toString(){
		String cardName;
		switch (this.value){
			case 1: 	cardName = "Ace"; 	break;
			case 11:	cardName = "Jack";	break;
			case 12:	cardName = "Queen";	break;
			case 13:	cardName = "King";	break;
			default:	cardName = String.valueOf(this.value);
		}
		return cardName + " of " + this.suit;
	}
	
	//Print card to console
	public void print(){
		System.out.println(this.toString());
	}
}
