package com.in28minutes.learnspringframework;

import com.in28minutes.learnspringframework.game.GameRunner;
import com.in28minutes.learnspringframework.game.PacmanGame;

public class App01GamingBasic {

	public static void main(String[] args) {

		// var game = new MarioGame();
		var game = new PacmanGame(); // 1: Object Creation
		// var game = new SuperContraGame();
		var gameRunner = new GameRunner(game);
		// 2: Object Creation + Wiring of Dependencies
		// Game is a Dependency of GameRunner
		gameRunner.run();

	}

}
