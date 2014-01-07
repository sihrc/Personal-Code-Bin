/**
 * Standard Black Jack Game
 * Dealer included
 */
package cardgames;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author clee2
 *
 */
public class BlackJack {
	//Scanner receives input from console
	private Scanner userInput; 
	//Initializing hands of player and dealer
	Hand player, dealer;
	Boolean dealerMove;
	Boolean playerMove;
	//Initializing Card Deck
	Deck52 deck;
	//Game Still in Session?
	Boolean end;
	//Public Constructor - to avoid making static references
	public BlackJack(){}
	
	//Main Method run
	public static void main(String[] args) {
		BlackJack game = new BlackJack();
		game.start();
	}
	
	private int start(){
		gameIntro();
		playerLoop();
		dealerLoop();
		print ("Game has ended. Play again? (y/n)");
		String response = userInput.next();
		if (response.equals("y")){
			this.deck.returnCards(this.dealer.hand);
			this.deck.returnCards(this.player.hand);
			this.deck.shuffle();
			this.start();
			return 0;
		} else {
			print ("See you again next time!");
			return 1;
		}
	}
	
	private void gameIntro(){
		//Start Listening
		userInput = new Scanner(System.in);
		end = false; //Start the game.
		print("Welcome to BlackJack!");
		//Create the deck
		this.deck = new Deck52();
		//Create the two hands
		this.player = new Hand("Player", -1);
		this.dealer = new Hand("Dealer", -1);
		//Add initial cards to the hands
		ArrayList<Card> drawn = this.deck.dealCards(4);
		//Player and Dealers receive alternate cards 
		this.dealer.addCard(drawn.get(1));
		this.dealer.addCard(drawn.get(3));
		this.player.addCard(drawn.get(0));
		this.player.addCard(drawn.get(2));
		//Both players are still playing
		playerMove = true;
		dealerMove = true;
	}
	
	private void playerLoop(){
		printStatus();
		if (!end){
			print("Hit (h)? Stay (s)?");
			String move = userInput.next();
			switch (move.toLowerCase()){
				case "h":
					print ("Player hits");
					this.player.addCard(this.deck.dealCards(1).get(0));
					this.playerLoop();
					break;
				case "s":
					print ("Player stays");
					break;
				default:
					print("Sorry. I didn't understand your input.");
					this.playerLoop();
			}
		}
	}

	private void dealerLoop(){
		printStatus();
		if (!end){
			Integer playerValue = calculateValue(this.player);
			Integer dealerValue = calculateValue(this.dealer);
			if (playerValue > 21){
				dealerMove = false;
			} else if (dealerValue < playerValue){
				print ("Dealer hits");
				this.dealer.addCard(this.deck.dealCards(1).get(0));
				this.dealerLoop();
			} else {
				print ("Dealer wins");
			}
		}
	}
	
	
	private void printStatus(){
		Integer dealerValue = calculateValue(this.dealer);
		Integer playerValue = calculateValue(this.player);
		
		print("=========================");
		print("Dealer's Hand");
		this.dealer.print();
		print("\t\tValue:" + dealerValue);
		print("Player's Hand");
		this.player.print();
		print("\t\tValue:" + playerValue);
		print("=========================");
		
		if (dealerValue > 21){
			print("Dealer over-hit! Player Wins!");
			end = true;
		} else if (playerValue > 21){
			print("Player over-hit! Dealer Wins!");
			end = true;
		} else if (dealerValue == 21){
			print("Dealer hits 21! Dealer wins!");
			end = true;
		} else if (playerValue == 21){
			print("Player hits 21! Player wins!");
		} 
	}
	
	private Integer calculateValue(Hand hand){
		Integer total = 0;
		Boolean hasAce = false;
		for (Card card:hand.hand){
			if (card.value == 1){
				hasAce = true;
			}
			total += card.value;
		}
		if (hasAce && total + 10 <= 21){
			total += 10;
		}
		return total;
	}
	private static void print(String message){
		System.out.println(message);
	}

}
