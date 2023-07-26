package com.in28minutes.learnspringframework.examples.business;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

//@Component
@Repository
@Primary
public class MongoDbDataService implements DataService {
	
	@Override
	public int[] retrieveData() {
		return new int[] {11, 22, 33, 44, 55};
	}
}
