package com.in28minutes.learnspringframework.game;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
public class SuperContraGame implements GamingConsole {

	@Override
	public void up() {
		System.out.println("up");
	}

	@Override
	public void down() {
		System.out.println("Sit down");
	}

	@Override
	public void left() {
		System.out.println("Go back");
	}

	@Override
	public void right() {
		System.out.println("Shoot a bullet");
	}
}
