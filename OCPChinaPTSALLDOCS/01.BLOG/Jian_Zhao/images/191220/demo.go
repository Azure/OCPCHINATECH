package main

import (
	"context"
	"time"
	"fmt"
	"log"
	"os"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/bson"
)

func main() {
 
	connStr := "mongodb://zjcosmos01:D3rqEKEVzZo4j1TAZ8RbpqDo6pAs6Rdfo4DBaxKEOun7Z5FmMGxAAlvstUfWNScoCjTCTL6Xa4VvJgcBTp6mEA==@zjcosmos01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@zjcosmos01@"

	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)

    client, err := mongo.Connect(ctx, options.Client().ApplyURI(connStr))

	if err != nil {
		fmt.Printf("Can't connect, go error %v\n", err)
		os.Exit(1)
	}

	defer client.Disconnect(ctx)

	// get collection
	collection := client.Database("zjcosmos01").Collection("package")
	
	// Insert Data
	res, err := collection.InsertOne(ctx, bson.M{"name": "pi", "value": 3.14159})
	
	if err != nil {
		fmt.Println("Problem inserting data: ", err)
		os.Exit(1)
	}
	
	id := res.InsertedID
	fmt.Println("Insert data succeeded with ID: ", id)
	log.Fatal("Insert data succeeded with ID: ", id)

	// Find Data
	cur, err := collection.Find(ctx, bson.D{})
	if err != nil { log.Fatal(err) }
	defer cur.Close(ctx)
	for cur.Next(ctx) {
	   var result bson.M
	   err := cur.Decode(&result)
	   if err != nil { log.Fatal(err) }
	   log.Fatal(result)
	}
	if err := cur.Err(); err != nil {
	  log.Fatal(err)
	}
}