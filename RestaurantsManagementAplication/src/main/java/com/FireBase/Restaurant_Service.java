package com.FireBase;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import org.springframework.stereotype.Service;

import java.util.concurrent.ExecutionException;

@Service
public class Restaurant_Service {



    public String create_Restaurant(Restaurant restaurant) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<DocumentReference> addedDocRef = db.collection("restaurants").add(restaurant);
        return "Restaurant added with ID: " + addedDocRef.get().getId();
    }

    public Restaurant get_Restaurant(String Name) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        return db.collection("restaurants").document(Name).get().get().toObject(Restaurant.class);
    }

    public String update_Restaurant(Restaurant restaurant) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> writeResult = db.collection("restaurants").document(restaurant.getName()).set(restaurant);
        return "Restaurant updated at: " + writeResult.get().getUpdateTime();
    }

    public String delete_Restaurant(String Name) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> deleteResult = db.collection("restaurants").document(Name).delete();
        return "Restaurant deleted at: " + deleteResult.get().getUpdateTime();
    }
}
