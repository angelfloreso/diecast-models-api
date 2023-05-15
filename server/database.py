import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.diecast

cars_collection = database.get_collection("cars_collection")

def cars_collection(carModel) -> dict:
    return {
        "id": str(carModel["_id"]),
        "code": carModel["code"],
        "fullname": carModel["fullname"],
        "category": carModel["category"],
        "year": carModel["year"],
    }