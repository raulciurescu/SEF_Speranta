package com.FireBase;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


import java.util.concurrent.ExecutionException;

@RestController
public class Restaurant_Controller {
    @Autowired
    Restaurant_Service restaurantService;

    public Restaurant_Controller(Restaurant_Service restaurantService){
        this.restaurantService = restaurantService;
    }

    @PostMapping(value = "/create")
    public String create_Restaurant(@RequestBody Restaurant restaurant) throws InterruptedException , ExecutionException{
       return restaurantService.create_Restaurant(restaurant);
    }

    @GetMapping("/get")
    public ResponseEntity<Object> get_Restaurant(@RequestParam String name) throws InterruptedException , ExecutionException{
        try {
            return ResponseEntity.ok(restaurantService.get_Restaurant(name));
        } catch (InterruptedException | ExecutionException e) {
            return ResponseEntity.status(500).body(null);
        }
    }

    @PutMapping("/update")
    public ResponseEntity<String> update_Restaurnat(@RequestBody Restaurant restaurant)throws  InterruptedException , ExecutionException{
        try {
            return ResponseEntity.ok(restaurantService.update_Restaurant(restaurant));
        } catch (InterruptedException | ExecutionException e) {
            return ResponseEntity.status(500).body("Error updating restaurant: " + e.getMessage());
        }
    }

    @PostMapping("/delete")
    public ResponseEntity<String> delete_Restaurant(@RequestParam String name) throws InterruptedException , ExecutionException{
        try {
            return ResponseEntity.ok(restaurantService.delete_Restaurant(name));
        } catch (InterruptedException | ExecutionException e) {
            return ResponseEntity.status(500).body("Error deleting restaurant: " + e.getMessage());
        }
    }
    @GetMapping("/api/test")
    public ResponseEntity<String> testEndpoint() {
        return ResponseEntity.ok("ba merge ceva");
    }
    @GetMapping("/error")
    public ResponseEntity<String> handleError() {
        return ResponseEntity.ok("ceva merge gresit");
    }

        @RequestMapping("/error")
		public String getErrorPath() {
			return "/error";
		}


}
