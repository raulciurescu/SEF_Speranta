package org.restaurantsmanagementaplication;

import java.util.Collections;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class RestaurantsManagementAplicationApplication {

	public static void main(String[] args) {
		SpringApplication app = new SpringApplication(RestaurantsManagementAplicationApplication.class);
		app.setDefaultProperties(Collections.singletonMap("server.port", "8080"));
		app.run(args);
	}
}
