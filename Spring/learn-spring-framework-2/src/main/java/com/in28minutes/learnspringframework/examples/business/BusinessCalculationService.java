package com.in28minutes.learnspringframework.examples.business;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;


//@Component
@Service
public class BusinessCalculationService {
	

	private DataService dataService;
	

	@Autowired
	public BusinessCalculationService(DataService dataService) {
		super();
		this.dataService = dataService;
	}


	public int findMax() {
		return Arrays.stream(dataService.retrieveData()).max().orElse(0);
	}
}
