package com.in28minutes.learnspringframework.game;

public class PacmanGame implements GamingConsole {

	@Override
	public void up() {
		System.out.println("Eat Up");
	}

	@Override
	public void down() {
		System.out.println("Eat Down");
	}

	@Override
	public void left() {
		System.out.println("Eat Left");
	}

	@Override
	public void right() {
		System.out.println("Eat Right");
	}

}
